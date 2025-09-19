import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def getcouponmatchescount(skinname: str='betbiga', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetCouponMatchesCount data api"
    
    """
    url = f"https://sport-odds1.p.rapidapi.com/sportsbook/getcouponmatchescount"
    querystring = {}
    if skinname:
        querystring['skinName'] = skinname
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sport-odds1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getevents(skinname: str='betbiga', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetEvents data api"
    
    """
    url = f"https://sport-odds1.p.rapidapi.com/sportsbook/getevents"
    querystring = {}
    if skinname:
        querystring['skinName'] = skinname
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sport-odds1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getallsports(skinname: str='betbiga', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetAllSports data api"
    
    """
    url = f"https://sport-odds1.p.rapidapi.com/sportsbook/getallsports"
    querystring = {}
    if skinname:
        querystring['skinName'] = skinname
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sport-odds1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getfavouriteschamps(skinname: str='betbiga', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetFavouritesChamps data api"
    
    """
    url = f"https://sport-odds1.p.rapidapi.com/sportsbook/getfavouriteschamps"
    querystring = {}
    if skinname:
        querystring['skinName'] = skinname
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sport-odds1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getupcoming(skinname: str='betbiga', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetUpcoming data api"
    
    """
    url = f"https://sport-odds1.p.rapidapi.com/sportsbook/getupcoming"
    querystring = {}
    if skinname:
        querystring['skinName'] = skinname
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sport-odds1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getliveevents(skinname: str='betbiga', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetLiveEvents data api"
    
    """
    url = f"https://sport-odds1.p.rapidapi.com/sportsbook/getliveevents"
    querystring = {}
    if skinname:
        querystring['skinName'] = skinname
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sport-odds1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def geteventtypes(skinname: str='betbiga', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetEventTypes data api"
    
    """
    url = f"https://sport-odds1.p.rapidapi.com/sportsbook/geteventtypes"
    querystring = {}
    if skinname:
        querystring['skinName'] = skinname
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sport-odds1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getlivenow(skinname: str='betbiga', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetLivenow data now"
    
    """
    url = f"https://sport-odds1.p.rapidapi.com/sportsbook/getlivenow"
    querystring = {}
    if skinname:
        querystring['skinName'] = skinname
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sport-odds1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getlivemenustreaming(skinname: str='betbiga', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetLiveMenuStreaming data api"
    
    """
    url = f"https://sport-odds1.p.rapidapi.com/sportsbook/getlivemenustreaming"
    querystring = {}
    if skinname:
        querystring['skinName'] = skinname
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sport-odds1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def geteventdetails(skinname: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetEventDetails api data"
    
    """
    url = f"https://sport-odds1.p.rapidapi.com/sportsbook/geteventdetails"
    querystring = {'skinName': skinname, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sport-odds1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def geteventexternalinfo(skinname: str='betbiga', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetEventExternalInfo data api"
    
    """
    url = f"https://sport-odds1.p.rapidapi.com/sportsbook/geteventexternalinfo"
    querystring = {}
    if skinname:
        querystring['skinName'] = skinname
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sport-odds1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getbreadcrumbnavitem(skinname: str='betbiga', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetBreadCrumbNavItem data api"
    
    """
    url = f"https://sport-odds1.p.rapidapi.com/sportsbook/getbreadcrumbnavitem"
    querystring = {}
    if skinname:
        querystring['skinName'] = skinname
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sport-odds1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def gettopsportmenu(skinname: str='betbiga', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetTopSportMenu data api"
    
    """
    url = f"https://sport-odds1.p.rapidapi.com/sportsbook/gettopsportmenu"
    querystring = {}
    if skinname:
        querystring['skinName'] = skinname
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sport-odds1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def gettopsports(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetTopSports data api"
    
    """
    url = f"https://sport-odds1.p.rapidapi.com/sportsbook/gettopsports"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sport-odds1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getmenubysport(skinname: str='betbiga', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetMenuBySport data api"
    
    """
    url = f"https://sport-odds1.p.rapidapi.com/sportsbook/getmenubysport"
    querystring = {}
    if skinname:
        querystring['skinName'] = skinname
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sport-odds1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getstatictranslations(skinname: str='betbiga', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetStaticTranslations data api"
    
    """
    url = f"https://sport-odds1.p.rapidapi.com/translation/getstatictranslations"
    querystring = {}
    if skinname:
        querystring['skinName'] = skinname
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sport-odds1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def gethighlights(skinname: str='betbiga', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetHighlights Data Api"
    
    """
    url = f"https://sport-odds1.p.rapidapi.com/sportsbook/gethighlights"
    querystring = {}
    if skinname:
        querystring['skinName'] = skinname
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sport-odds1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

