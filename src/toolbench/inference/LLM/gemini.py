if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    __package__ = "toolbench.inference.LLM"

from .openai_base_chat_model import openai_base_chat_model

import json
import time

class GeminiChatFunction(openai_base_chat_model, base_url_=""):
    def __init__(self, model="", openai_key="", temperature = 0):
        super().__init__(model, openai_key)
        self.temperature = temperature

    def chat_completion_request(self, messages, functions= None, tool_choice = None, stop=None, **args):
        self.name_map = {}
        self.real_to_fake = {}
        use_messages = []
        for message in messages:
            if not("valid" in message.keys() and message["valid"] == False):
                use_messages.append(message)

        for id, message in enumerate(use_messages):
            if 'name' in message and len(message['name']) > 63:
                use_messages[id]['name'] = message['name'][:63]

            if 'tool_calls' in message and message['tool_calls'] is not None and len(message['tool_calls']) > 0:
                for i, tool in enumerate(message['tool_calls']):
                    if len(message['tool_calls'][i]['function']['name']) > 63:
                        use_messages[id]['tool_calls'][i]['function']['name'] = message['tool_calls'][i]['function']['name'][:63]

        for id, message in enumerate(use_messages):
            if 'role' in message and message['role'] == 'tool':
                use_messages[id]['role'] = 'user'
                use_messages[id]['content'] = f"The tool output is {message['content']}, remember to call Finish tool when either if you believe that you have obtained a result that can answer the task, please call this function to provide the final answer. Alternatively, if you recognize that you are unable to proceed with the task in the current state, call this function to restart. Remember: you must ALWAYS call this function at the end of your attempt, and the only part that will be shown to the user is the final answer, so it should contain sufficient information."

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
                function_name = function["name"]
                if len(function_name) > 63:
                    fake_name = function_name[:63]
                    self.name_map[fake_name] = function_name
                    self.real_to_fake[function_name] = fake_name
                    function["name"] = fake_name

                if "parameters" in function.keys():
                    if "properties" in function["parameters"].keys():
                        if len(function["parameters"]["properties"]) == 0:
                            continue

                        else:
                            for key, item in function["parameters"]["properties"].items():
                                if 'example_value' in item.keys():
                                    del function["parameters"]["properties"][key]['example_value']


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
            return self.chat_completion_request(messages, functions, tool_choice, stop, **args)

    def parse(self,functions,tool_choice, process_id,**args):
        '''
        This function is used to parse the input into the satisfied format for the chat_completion_request function and run it. 
        '''
        self.time = time.time()
        conversation_history = self.conversation_history

        for _ in range(self.TRY_TIME):
            if functions != []:
                json_data = self.chat_completion_request(
                    conversation_history, functions=functions,tool_choice = tool_choice, **args
                )
            else:
                json_data = self.chat_completion_request(
                    conversation_history, tool_choice = tool_choice,process_id=process_id,**args
                )
            try:
                total_tokens = json_data['usage']['total_tokens']
                message = json_data["choices"][0]["message"]
                if process_id == 0:
                    print(f"[process({process_id})]total tokens: {json_data['usage']['total_tokens']}")

                if "tool_calls" in message.keys() and message["tool_calls"] is not None:
                    for i, tool in enumerate(message["tool_calls"]):
                        if '.' in tool['function']['name']:
                            message["tool_calls"][i]['function']['name'] = tool['function']['name'].split(".")[-1]
                    
                    for i, tool in enumerate(message["tool_calls"]):
                        if tool['function']['name'] in self.name_map.keys():
                            message["tool_calls"][i]['function']['name'] = self.name_map[tool['function']['name']]

                return message, 0, total_tokens
            except BaseException as e:
                print(f"[process({process_id})]Parsing Exception: {repr(e)}. Try again.")
                if json_data is not None:
                    print(f"[process({process_id})]OpenAI return: {json_data}")


        return {"role": "assistant", "content": str(json_data)}, -1, 0
