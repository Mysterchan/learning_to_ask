import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def member_details(memberid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "With this endpoint you can find member information about a specific player."
    
    """
    url = f"https://laserforce-statistics.p.rapidapi.com/memberdetails.php"
    querystring = {'memberId': memberid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "laserforce-statistics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def recent_missions(limit: int, memberid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "With this endpoint you can view a player's last 30 missions."
    
    """
    url = f"https://laserforce-statistics.p.rapidapi.com/recentmissions.php"
    querystring = {'limit': limit, 'memberId': memberid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "laserforce-statistics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def last_5_recent_missions(memberid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "With this endpoint you can view a player's last 5 missions."
    
    """
    url = f"https://laserforce-statistics.p.rapidapi.com/recent5missions.php"
    querystring = {'memberId': memberid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "laserforce-statistics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

