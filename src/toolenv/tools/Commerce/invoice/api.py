import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def para(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "yes we are"
    
    """
    url = f"https://invoice2.p.rapidapi.com/qr/custom?data=https%3a%2f%2fwww.qrcode-monkey.com&size=600&file=png&config=%7b%22bodycolor%22%3a%20%22%230277bd%22%2c%20%22body%22%3a%22mosaic%22%7d"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "invoice2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

