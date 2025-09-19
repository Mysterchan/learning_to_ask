import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def getgamedetailpro(is_id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the game's information as Json."
    
    """
    url = f"https://evosiss-game-database.p.rapidapi.com/getgamedetailpro/proxap3mptgydcbsaeyaiaksajorsc54/{is_id}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "evosiss-game-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getgamedetail(is_id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the game's information as Json"
    
    """
    url = f"https://evosiss-game-database.p.rapidapi.com/getgamedetail/advencexp3mptgydcbsaeya3gxaod5b9/{is_id}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "evosiss-game-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getstorestatuslist(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns as Json of store status list."
    
    """
    url = f"https://evosiss-game-database.p.rapidapi.com/getstorestatuslist/ldlap3mptgydcbsaeyai2mgmnqmod5bk/"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "evosiss-game-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getplatformlist(page: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the id and names of the platforms as Json."
    
    """
    url = f"https://evosiss-game-database.p.rapidapi.com/getplatformlist/ldlap3mptgydcbsaeyai2mgmnqmod5bk/{page}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "evosiss-game-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getgamelist(page: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the ID and series names of the games as Json."
    
    """
    url = f"https://evosiss-game-database.p.rapidapi.com/getgamelist/ldlap3mptgydcbsaeyai2mgmnqmod5bk/{page}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "evosiss-game-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

