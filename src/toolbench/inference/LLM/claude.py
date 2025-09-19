if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    __package__ = "toolbench.inference.LLM"

from .openai_base_chat_model import openai_base_chat_model

import json

class ClaudeChatFunction(openai_base_chat_model, base_url_=""):
    def __init__(self, model="", openai_key="", temperature = 0):
        super().__init__(model, openai_key)
        self.temperature = temperature


    def chat_completion_request(self, messages, functions= None, tool_choice = None, stop=None, **args):
        use_messages = []
        for message in messages:
            if not("valid" in message.keys() and message["valid"] == False):
                use_messages.append(message)

        json_data = {
            "model": self.model,
            "messages": use_messages,
            "max_tokens": 1024,
            'frequency_penalty': 0,
            'presence_penalty': 0,
            'temperature': self.temperature,
        }

        if stop is not None:
            json_data.update({"stop": stop})
        if functions is not None:
            tools = []
            for function in functions:
                if "parameters" in function.keys():
                    if "optional" in function["parameters"].keys():
                        del function["parameters"]["optional"]

                tool = {
                    "type": "function",
                    "function": function
                }
                tools.append(tool)

            json_data.update({"tools": tools})
        if tool_choice is not None:
            json_data.update({"tool_choice": tool_choice})

        try:
            response = self.client.chat.completions.create(
                **json_data
            )
            json_data = response.model_dump_json()
            return json.loads(json_data)
        
        except Exception as e:
            print("Unable to generate ChatCompletion response")
            print(f"OpenAI calling Exception: {e}")
            return e