if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    __package__ = "toolbench.tooleval"

import json
import argparse
import openai
import backoff
import asyncio
import csv 
import tqdm
import time

from toolbench.inference.LLM.LLM_funtion_model import SimpleLLMChatFunction

class OutOfQuotaException(Exception):
    "Raised when the key exceeded the current quota"
    def __init__(self, key, cause=None):
        super().__init__(f"No quota for key: {key}")
        self.key = key
        self.cause = cause

    def __str__(self):
        if self.cause:
            return f"{super().__str__()}. Caused by {self.cause}"
        else:
            return super().__str__()


class AccessTerminatedException(Exception):
    "Raised when the key has been terminated"
    def __init__(self, key, cause=None):
        super().__init__(f"Access terminated key: {key}")
        self.key = key
        self.cause = cause

    def __str__(self):
        if self.cause:
            return f"{super().__str__()}. Caused by {self.cause}"
        else:
            return super().__str__()


def parse_args():
    parser = argparse.ArgumentParser("", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-folder", "--result_folder", type=str, required=True,
        help="result folder path")
    parser.add_argument("-data", "--data_path", type=str, required=True,
        help="instruciton data path")
    parser.add_argument("-csv", "--csv_statistics_file", type=str, required=True,
        help="the csv statistics file ")
    parser.add_argument("-ori", "--original", type=bool, default=False)
    parser.add_argument("-key", "--key", type=str, required=True)
    parser.add_argument("-model", "--model_selection", type=str, default="GPT4")
    parser.add_argument("-base_url", "--base_url", type=str, default="")
    
    return parser.parse_args()

EVALUATOR_PROMPT = """As an evaluator of tool-augmented language model systems, your responsibility is to assess the models' effectiveness
in using APIs to gather necessary information to fulfill user requests. This involves reviewing the actual API calls made by the enhanced
models against a given set of required API calls, including their parameters. Your evaluation focuses on two main objectives:

Objective 1: Verify the accuracy of the actual tool calls made by the enhanced models against the expected tool calls, including their arguments. 
A successful outcome means that the models executed all required API calls with expected arguments. Otherwise, it is a failure for Objective 1.

The following are some important guidance for evaluation of Objective 1:
1.The actual tool call is allowed to include additional parameters that are not required in the expected tool call. The additional parameters will not affect the correctness of the tool call if tool name and all the required arguments are correct(In another word, we can also consider it as a success for this kind of situation!!!). 
2.We do not care the response. We only care the accuracy of tool name and their corresponding arguments. 
3.Due to some technical issues, some of the tool name are truncated and some are the argument name are not exactly the same, you need to be smart to judge the correctness of the tool call. 
4.The model is allowed to invoke additional unnecessary tools that do not align with our expected tools. We only need to check whether all the expected tool calls are invoked, if yes, then it is a success.
5.The order of tool call does not matter for Objective 1.
6.The model is allowed to invoke tools that are not required.
or
Below is an example:
Example 1:
the following is the tool invoked by the model:
 'search_image_for_google_search_json' with arguments '{\n  "q": "beaches in Hawaii",\n  "num": 5\n}'
the following is the required API call:
"expected API calling": 'search_image_for_google_search_json' with arguments '{\n  "q": "Hawaii"\n  }'

For above example, even the argument "q" is not the same, both tool calls intend to search the image of 'Hawaii', and the additional argument "num"
does not affect the intention of the tool call, we consider above example is a success for Objective 1.
However, if the argument "q" spell 'Hawaii' wrong like 'Hawii', we consider above example is a failure for Objective 1.
We accept very close semantic meaning, for example, 'beaches in Hawaii' and 'Hawaii' are considered as the same meaning, but spelling mistakes are not allowed.

Example 2:
the following is the tool invoked by the model:
'get_address_transactions_for_address_monitor' with '{\n  "monitorAddressId": "0x71C7656EC7ab88b098defB751B7401B5f6d8976F"\n }'
the following is the required API call:
'get_address_transactions_for_address_monitor' with '{\n  "monitorAddressId": "8485d9c3-7f52-4ba7-8ec2-41543effa6ae"\n }'

For above example, the tool name is correct, but the argument "monitorAddressId" is not the same, we consider above example is a failure for Objective 1.

Please be reminded that the model will have additional unnecessary tools that do not align with our expected tools. We only need to check whether all the expected tool calls are invoked, if yes, then it is a success.

Objective 2: Assess whether the model's final response correctly achieve the user's instruction and check if the final answer was indeed based on the
data retrieved from these API calls, as opposed to being generated independently of these tool calls. Success in this objective means the
model effectively used the API calls to achieve user's instructions. Conversely, failure suggests the response was not derived from the API 
data or the user's instruction is not achieved. It's important to note that any thoughts of the LLMs not based on the API response, especially
regarding makeup information, are not considered valid answers. Please note that if the model does not provide the final answer, we consider it as a failure case.

You need to pay attention to the following rule: 
If the Objective 1 is a failure, we can directly infer that Objective 2 is also a failure. However, the objective 1 is independent of objective 2. That means if 
Objective 2 is a failure does not imply Objective 1 is a failure.

Your evaluation should be summarized as follows(Please follow below format and start a new line for each objective and reason):

Objective 1: Success or Failure
Objective 2: Success or Failure
Reason: ...(for the reasons, you need to give the details. For example, if the Objective 1 is successfully achieved, you need to give both the tools invoked by the model and 
the expected tool calls. Then, you should compare them to give the result)



"""

class AutoEvaluator:
    def __init__(self, data, result_foler, original, AI_model, key, base_url) -> None:
        '''
        data: unclear/ incorrect/ ... file
        result_foler: the folder containing the log.json files
        original: whether the data is original or not (if is original, then the data is not using the interaction prompt)
        AI_model: the model used for the evaluation (ChatGPT or GPT4)
        '''
        self.data = data
        self.result_foler = result_foler
        self.expected_api_stat = {}
        self.stat = {}
        self.count = 0
        self.original = original
        if AI_model == "ChatGPT":
            self.AI_model = SimpleLLMChatFunction('gpt-3.5-turbo', key, base_url_=base_url)
        elif AI_model == "deepseek":
            self.AI_model = SimpleLLMChatFunction('deepseek-chat', key, base_url_=base_url)
        elif AI_model == "gpt4o":
            self.AI_model = SimpleLLMChatFunction('gpt-4o-2024-11-20', key, base_url_=base_url)
        else:
            try:
                self.AI_model = SimpleLLMChatFunction(AI_model, key, base_url_=base_url)
            except:
                print(f"[ERROR] Model {AI_model} is not supported for {base_url}")
                exit(1)

    def load_expected_api_call(self):
        with open(self.data, 'r', encoding="utf-8") as file:
            answer = json.load(file)
        for i in range(len(answer)):
            self.expected_api_stat[i+1] = answer[i]['expected API calling']

    def translate_with_backoff(self, messages):
        self.AI_model.change_messages(messages)
        retries = 5
        while retries > 0:
            try:
                gen, error, total_token = self.AI_model.parse(None, None, 1)
                if error:
                    raise Exception("OpenAI API calling exception")
                if not gen['content']:
                    raise Exception("Empty response from OpenAI")
                return gen['content'].strip().replace('\n\n\n', '\n\n')
            except openai.RateLimitError as e:
                retry_after = int(e.headers.get("Retry-After", 10)) if e.headers and "Retry-After" in e.headers else 10
                print(f"Rate limit reached. Retrying after {retry_after} seconds...")
                time.sleep(retry_after)
            
            except openai.APIConnectionError:
                print("API connection error. Retrying in 10 seconds...")
                time.sleep(10)
            
            except Exception as e:
                print(f"Exception occurred: {e}. Retrying in 10 seconds...")
                time.sleep(10)
            retries -= 1
        raise Exception("Failed to call OpenAI API after retries")


    def get_messages(self, interaction_history, expected_API_calls):
        messages = []
        messages.append(
            {"role": "system", "content": EVALUATOR_PROMPT}
        )
        user_prompt = """
            Below is what I require you to evaluate:
            the dict containting "'tool_calls'" gives the tool invoked by the model;
            the dict containing "'role': 'tool'" gives the response of the invoked tool;
            the dict containing "'return_type': 'give_answer',  'final_answer'" gives the final answer to the user's instruction (To evaluate objective 2, you need to evaluate if the given answer fulfil the requirement)(It is possible that "give answer" does not appear below. It means the model did not give the final answer, and you can directly consider it fails to fulfil objective 2. Also, if the objective 1 fails, you can directly consider objective 2 fails).
            {interaction_history}
            Below is the required API calls (To evaluate objective 1, you need to compare the required API calls and the actual tool calls invoked by the model(what has been shown above)):
            {expected_API_calls}
        """
        history = []
        for element in interaction_history:
            if "tool_calls" in element or element["role"] == "tool":
                history.append(element)
        
        history = list({json.dumps(d, sort_keys=True): d for d in history}.values())
        user_prompt = user_prompt.format(interaction_history=str(history), expected_API_calls=expected_API_calls)
        
        messages.append(
            {"role": "user", "content": user_prompt}
        )
        return messages


    def evaluate_question_asking(self):
        for filename in os.listdir(self.result_foler):
            if filename.endswith('.json') and not filename.endswith('log.json'):
                index = filename.split('_')[0]
                self.stat[int(index)] = {}
                file_path = os.path.join(self.result_foler, filename)
                with open(file_path, 'r') as file:
                    result = json.load(file)
                if result['ask_corresponding_question']:
                    self.stat[int(index)]['goal1'] = 'Success'
                else:
                    self.stat[int(index)]['goal1'] = 'Failure'
                if not self.original:
                    self.stat[int(index)]['redundant_ask_count'] = result['redundant_ask_count']
                self.stat[int(index)]['query'] = result['answer_generation']['query'] 
                
        total = 0
        for key, value in self.stat.items():
           print(key, value)
           total += value['goal1'] == 'Success'
        print(f"[INFO] The accuracy for question asking is {total/len(self.stat)}")


    def evaluate_api_call_final_result(self):
        file_exists = os.path.exists(filename)
        if file_exists:
            # check whole first columns to get query_id
            query_id_set = []
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in list(reader)[1:]:
                    query_id_set.append(row[0])

        for filename in os.listdir(self.result_foler):
            if filename.endswith('log.json'):
                if file_exists and filename.split('_')[0] in query_id_set:
                    continue
                print("[INFO]Processing: "+filename)
                index = filename.split('_')[0]
                file_path = os.path.join(self.result_foler, filename)
                with open(file_path, 'r') as file:
                    interaction_history = json.load(file)
                expected_API_calls = self.expected_api_stat.get(int(index))
                messages = self.get_messages(interaction_history, expected_API_calls)

                a = 1
                while a == 1:
                    try:
                        gen = self.translate_with_backoff(
                                    messages=messages,
                                )
                        goal1 = gen.split('\n')[0]
                        goal2 = gen.split('\n')[1]
                        reason = gen.split('\n')[2:]
                        reason = '\n'.join(reason)
                        a = 2
                    except Exception as e:
                        print(f"Exception occurred: {e}. Retrying in 5 seconds...")
                        time.sleep(5)
                        continue
                self.count += 1
                cnt = 0
                for item in interaction_history:
                    if item['role'] == 'assistant':
                       cnt += 1 
                        
                self.stat[int(index)]['goal2'] = goal1  
                self.stat[int(index)]['goal3'] = goal2  
                self.stat[int(index)]['steps'] = cnt
                self.stat[int(index)]['reason'] = reason.replace("Objective 2","Objective 3")
                self.stat[int(index)]['reason'] = self.stat[int(index)]['reason'].replace("Objective 1","Objective 2")
                print("Goal 2: " + goal1)
                print("Goal 3: " + goal2)
                print(self.stat[int(index)]['reason'])
    

    def final_statistics(self):
        self.stat = {key: self.stat[key] for key in sorted(self.stat)}

        size = len(self.stat)
        goal1_size = 0
        goal2_size = 0
        goal3_size = 0
        for key, value in self.stat.items():
            # check whether stat['goal1'] this sentence contain success this word, lower
            if 'success' in value['goal1'].lower():
                goal1_size += 1
            if 'success' in value['goal2'].lower():
                goal2_size += 1
            if 'success' in value['goal3'].lower():
                goal3_size += 1
        print(f"[INFO] The final accuracy for goal1 is {goal1_size/size}")
        print(f"[INFO] The final accuracy for goal2 is {goal2_size/size}")
        print(f"[INFO] The final accuracy for goal3 is {goal3_size/size}")
                

    def write_results(self, filename) -> None:
        folder = []
        if '/' in filename:
            folder = filename.split('/')
        folder_name = ""
        flag = False 
        count = 0
        if len(folder) > 1:
            for item in folder:
                count += 1
                if count < len(folder):
                    if flag: 
                        folder_name = folder_name + "/" + item
                    else:
                        folder_name = item
                    flag = True
                    if not os.path.exists(folder_name):
                        os.mkdir(folder_name)

        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=",")
            if not self.original:
                writer.writerow(["query_id", "query", "steps", "redundant_asking","goal1", "goal2", "goal3", "reason"])
                for key, item in self.stat.items():
                    query_id = key
                    query = item['query']
                    steps = item["steps"]
                    redundant_asking = item['redundant_ask_count']
                    goal1 = item["goal1"]
                    goal2 = item["goal2"]
                    goal3 = item["goal3"]
                    reason = item["reason"]
                    writer.writerow([query_id, query, steps, redundant_asking, goal1, goal2, goal3, reason])
            else:
                writer.writerow(["query_id", "query", "steps", "goal1", "goal2", "goal3", "reason"])
                for key, item in self.stat.items():
                    query_id = key
                    query = item['query']
                    steps = item["steps"]
                    goal1 = item["goal1"]
                    goal2 = item["goal2"]
                    goal3 = item["goal3"]
                    reason = item["reason"]
                    writer.writerow([query_id, query, steps, goal1, goal2, goal3, reason])

    def append_results(self, filename, query_id, item):
        file_exists = os.path.exists(filename)  # Check if file exists to write headers only once

        with open(filename, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=",")
            
            # Write headers only if the file doesn't exist
            if not file_exists:
                if not self.original:
                    writer.writerow(["query_id", "query", "steps", "redundant_asking", "goal1", "goal2", "goal3", "reason"])
                else:
                    writer.writerow(["query_id", "query", "steps", "goal1", "goal2", "goal3", "reason"])

            # Write the data row
            query = item['query']
            steps = item["steps"]
            if not self.original:
                redundant_asking = item.get('redundant_ask_count', '-')
                goal1 = item["goal1"]
                goal2 = item["goal2"]
                goal3 = item["goal3"]
                reason = item["reason"]
                writer.writerow([query_id, query, steps, redundant_asking, goal1, goal2, goal3, reason])
            else:
                goal1 = item["goal1"]
                goal2 = item["goal2"]
                goal3 = item["goal3"]
                reason = item["reason"]
                writer.writerow([query_id, query, steps, goal1, goal2, goal3, reason])

    def evaluate_api_call_per_result(self, csv_filename=None):
        file_exists = os.path.exists(csv_filename)
        if file_exists:
            # check whole first columns to get query_id
            query_id_set = []
            with open(csv_filename, 'r', encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in list(reader)[1:]:
                    query_id_set.append(row[0])
        for filename in os.listdir(self.result_foler):
            if filename.endswith('log.json'):
                if file_exists and filename.split('_')[0] in query_id_set:
                    continue
                print("[INFO]Processing: " + filename)
                index = filename.split('_')[0]
                file_path = os.path.join(self.result_foler, filename)
                with open(file_path, 'r') as file:
                    interaction_history = json.load(file)
                expected_API_calls = self.expected_api_stat.get(int(index))
                messages = self.get_messages(interaction_history, expected_API_calls)
                a = 1
                while a == 1:
                    try:
                        gen = self.translate_with_backoff(
                            messages=messages,
                        )
                        goal1 = gen.split('\n')[0].split(':')[1].strip()
                        goal2 = gen.split('\n')[1].split(':')[1].strip()
                        reason = gen.split('\n')[2:]
                        reason = '\n'.join(reason)
                        a = 2
                    except Exception as e:
                        print(f"Exception occurred: {e}. Retrying in 5 seconds...")
                        time.sleep(5)
                        continue
                self.count += 1
                cnt = 0
                for item in interaction_history:
                    if item['role'] == 'assistant':
                        cnt += 1

                self.stat[int(index)]['goal2'] = goal1  
                self.stat[int(index)]['goal3'] = goal2  
                self.stat[int(index)]['steps'] = cnt
                self.stat[int(index)]['reason'] = reason.replace("Objective 2","Objective 3")
                self.stat[int(index)]['reason'] = self.stat[int(index)]['reason'].replace("Objective 1","Objective 2")
                print("Goal 2: " + goal1)
                print("Goal 3: " + goal2)
                print(self.stat[int(index)]['reason'])

                # Append results to CSV file if a filename is provided
                if csv_filename:
                    self.append_results(csv_filename, int(index), self.stat[int(index)])


if __name__ == "__main__":
    args = parse_args()
    evaluator = AutoEvaluator(args.data_path, args.result_folder, args.original, args.model_selection, args.key, args.base_url)
    evaluator.load_expected_api_call()
    evaluator.evaluate_question_asking()
    # evaluator.evaluate_api_call_per_result(args.csv_statistics_file)
    # evaluator.final_statistics()
    # evaluator.write_results(args.csv_statistics_file)  # Ensure you pass the correct arguments to write_results
