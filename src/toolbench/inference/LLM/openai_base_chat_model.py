from openai import OpenAI
import json
import abc
import time
from termcolor import colored

class openai_base_chat_model:
    base_url_ = ""  # Placeholder for subclass-specific base_url_

    def __init__(self, model="", openai_key="") -> None:
        '''
        This class is the base class for all chat endpoints supporting openai sdk.  (gpt/ deepseek/ etc.)
        model: name of the model
        openai_key: openai api key

        conversation_history: list of messages (a tuple, role: str, content: str) in the conversation
        '''
        super().__init__()
        self.model = model
        self.conversation_history = []
        self.openai_key = openai_key
        self.base_url = type(self).base_url_
        self.time = time.time()
        self.TRY_TIME = 6
        self.client = OpenAI(api_key=openai_key, base_url=self.base_url)  # Initialize OpenAI client here

    def __init_subclass__(cls, base_url_, **kwargs):
        '''
        This method is called when a new subclass is created. It enforces that each subclass
        specifies its own base_url_.
        '''
        super().__init_subclass__(**kwargs)
        if not base_url_:
            raise ValueError(f"Subclass {cls.__name__} must define a non-empty base_url_.")
        cls.base_url_ = base_url_  # Assign the base_url_ to the subclass

    def add_message(self, message):
        self.conversation_history.append(message)

    def change_messages(self, messages):
        self.conversation_history = messages

    def display_conversation(self, detailed=False):
        role_to_color = {
            "system": "red",
            "user": "green",
            "assistant": "blue",
            "function": "magenta",
        }
        print("before_print" + "*" * 50)
        for message in self.conversation_history:
            print_obj = f"{message['role']}: {message['content']} "
            if "function_call" in message.keys():
                print_obj = print_obj + f"function_call: {message['function_call']}"
            print_obj += ""
            print(
                colored(
                    print_obj,
                    role_to_color[message["role"]],
                )
            )
        print("end_print" + "*" * 50)

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
            if _ != 0:
                time.sleep(15)
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

                return message, 0, total_tokens
            except BaseException as e:
                print(f"[process({process_id})]Parsing Exception: {repr(e)}. Try again.")
                if json_data is not None:
                    print(f"[process({process_id})]OpenAI return: {json_data}")


        return {"role": "assistant", "content": str(json_data)}, -1, 0