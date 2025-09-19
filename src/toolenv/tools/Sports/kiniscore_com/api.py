import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_all_teams(client: str, secret: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return all the Teams in json format"
    
    """
    url = f"https://kiniscore-com.p.rapidapi.com/getallteams.php"
    querystring = {'client': client, 'secret': secret, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiniscore-com.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_all_past_fixtures(secret: str, client: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return all the Past Fixtures"
    
    """
    url = f"https://kiniscore-com.p.rapidapi.com/getpastfixtures.php"
    querystring = {'secret': secret, 'client': client, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiniscore-com.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_all_upcoming_fixtures(secret: str, client: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return all the upcoming fixtures in json"
    
    """
    url = f"https://kiniscore-com.p.rapidapi.com/getupcomingfixtures.php"
    querystring = {'secret': secret, 'client': client, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiniscore-com.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_single_fixture(secret: str, client: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns Single Fixtures in json"
    
    """
    url = f"https://kiniscore-com.p.rapidapi.com/getsinglefixture.php"
    querystring = {'secret': secret, 'client': client, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiniscore-com.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_single_team(secret: str, client: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns single team details in json"
    
    """
    url = f"https://kiniscore-com.p.rapidapi.com/getsingleteam.php"
    querystring = {'secret': secret, 'client': client, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiniscore-com.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_team_squad(secret: str, client: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns full Squad of a Team in json"
    
    """
    url = f"https://kiniscore-com.p.rapidapi.com/getteamsquad.php"
    querystring = {'secret': secret, 'client': client, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiniscore-com.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_single_player(secret: str, client: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns full Detail of a Player in json"
    
    """
    url = f"https://kiniscore-com.p.rapidapi.com/getsingleplayer.php"
    querystring = {'secret': secret, 'client': client, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiniscore-com.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_team_fixtures(client: str, secret: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns Fixtures of a Team in json"
    
    """
    url = f"https://kiniscore-com.p.rapidapi.com/getteamfixtures.php"
    querystring = {'client': client, 'secret': secret, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiniscore-com.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_team_past_fixtures(secret: str, client: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns Fixtures of a Team in Past json"
    
    """
    url = f"https://kiniscore-com.p.rapidapi.com/getteampastfixtures.php"
    querystring = {'secret': secret, 'client': client, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiniscore-com.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_table_standings(secret: str, client: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns table standings in json"
    
    """
    url = f"https://kiniscore-com.p.rapidapi.com/gettablestandings.php"
    querystring = {'secret': secret, 'client': client, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiniscore-com.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_all_fixtures(secret: str, client: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Gets All Fixtures"
    
    """
    url = f"https://kiniscore-com.p.rapidapi.com/getallfixtures.php"
    querystring = {'secret': secret, 'client': client, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiniscore-com.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def all_fixtures(client: str, secret: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "To get all match fixtures in json format"
    
    """
    url = f"https://kiniscore-com.p.rapidapi.com/allfixtures.php"
    querystring = {'client': client, 'secret': secret, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiniscore-com.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_all_leagues(client: str, secret: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "To get all leagues in json format"
    
    """
    url = f"https://kiniscore-com.p.rapidapi.com/getallleague.php"
    querystring = {'client': client, 'secret': secret, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiniscore-com.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

