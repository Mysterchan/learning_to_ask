import requests
import json
 
# DeepSeek API的文本生成端点
url = "https://api.deepseek.com/chat/completions"
 
# 您的API密钥
api_key = "sk-ea4c0fa648024a4c96f8dccb6ada44cf"  # 请替换为您的API密钥
 
# 请求头
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
 
# 请求数据
data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    "stream": False
}
 
try:
    # 发送POST请求
    response = requests.post(url, headers=headers, data=json.dumps(data), timeout=100)
    print(response.text.__repr__())
    while response.text == "":
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=100)
        print(response.text.__repr__())
    response.raise_for_status()  # 检查响应状态码
 
    # 解析响应数据
    result = response.json()
 
    # 打印生成的内容
    if "choices" in result and len(result["choices"]) > 0:
        print(result["choices"][0]["message"]["content"])
 
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    print(f"Response status code: {response.status_code}")
    print(f"Response text: {response.text}")
 
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
 
except Exception as err:
    print(f"An error occurred: {err}")