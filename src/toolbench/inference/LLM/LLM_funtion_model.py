if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    __package__ = "toolbench.inference.LLM"

from .openai_base_chat_model import openai_base_chat_model

import json
import requests

class ChatGPTChatFunction(openai_base_chat_model, base_url_=""):
    def __init__(self, model="", openai_key="", temperature = 0):
        super().__init__(model, openai_key)
        self.temperature = temperature
