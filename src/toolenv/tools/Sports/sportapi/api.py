import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def getstatictranslations(origin: str='https://fullreto.co', referer: str='https://fullreto.co/', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetStaticTranslations Api Data"
    
    """
    url = f"https://sportapi1.p.rapidapi.com/api/translation/getstatictranslations"
    querystring = {}
    if origin:
        querystring['Origin'] = origin
    if referer:
        querystring['referer'] = referer
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportapi1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def geteventtrackerinfo(referer: str='https://fullreto.co/', origin: str='https://fullreto.co', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetEventTrackerInfo data api"
    
    """
    url = f"https://sportapi1.p.rapidapi.com/api/sportsbook/geteventtrackerinfo"
    querystring = {}
    if referer:
        querystring['Referer'] = referer
    if origin:
        querystring['Origin'] = origin
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportapi1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getmenubysport(referer: str='https://fullreto.co', origin: str='https://fullreto.co', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetMenuBySport api data"
    
    """
    url = f"https://sportapi1.p.rapidapi.com/api/sportsbook/getmenubysport"
    querystring = {}
    if referer:
        querystring['Referer'] = referer
    if origin:
        querystring['Origin'] = origin
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportapi1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def geteventtypes(origin: str='https://fullreto.co', referer: str='https://fullreto.co/', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetEventTypes  data api"
    
    """
    url = f"https://sportapi1.p.rapidapi.com/api/sportsbook/geteventtypes"
    querystring = {}
    if origin:
        querystring['Origin'] = origin
    if referer:
        querystring['Referer'] = referer
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportapi1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getevents(referer: str='https://fullreto.co/', origin: str='https://fullreto.co', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetEvents data api"
    
    """
    url = f"https://sportapi1.p.rapidapi.com/api/sportsbook/getevents"
    querystring = {}
    if referer:
        querystring['Referer'] = referer
    if origin:
        querystring['Origin'] = origin
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportapi1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getbreadcrumbnavitem(origin: str='https://fullreto.co', referer: str='https://fullreto.co/', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetBreadCrumbNavItem  api data"
    
    """
    url = f"https://sportapi1.p.rapidapi.com/api/sportsbook/getbreadcrumbnavitem"
    querystring = {}
    if origin:
        querystring['Origin'] = origin
    if referer:
        querystring['Referer'] = referer
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportapi1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getlivemenustreaming(referer: str='https://fullreto.co/', origin: str='https://fullreto.co', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetLiveMenuStreaming api data"
    
    """
    url = f"https://sportapi1.p.rapidapi.com/api/sportsbook/getlivemenustreaming"
    querystring = {}
    if referer:
        querystring['Referer'] = referer
    if origin:
        querystring['origin'] = origin
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportapi1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def geteventdetails(referer: str='https://fullreto.co/', origin: str='https://fullreto.co', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetEventDetails api data"
    
    """
    url = f"https://sportapi1.p.rapidapi.com/api/sportsbook/geteventdetails"
    querystring = {}
    if referer:
        querystring['Referer'] = referer
    if origin:
        querystring['Origin'] = origin
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportapi1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def geteventexternalinfo(origin: str='https://fullreto.co', referer: str='https://fullreto.co/', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetEventExternalInfo api data"
    
    """
    url = f"https://sportapi1.p.rapidapi.com/api/sportsbook/geteventexternalinfo"
    querystring = {}
    if origin:
        querystring['Origin'] = origin
    if referer:
        querystring['Referer'] = referer
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportapi1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def gettopsports(origin: str='https://fullreto.co', referer: str='https://fullreto.co/', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetTopSports api data"
    
    """
    url = f"https://sportapi1.p.rapidapi.com/api/sportsbook/gettopsports"
    querystring = {}
    if origin:
        querystring['Origin'] = origin
    if referer:
        querystring['Referer'] = referer
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportapi1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getallsports(referer: str='https://fullreto.co/', origin: str='https://fullreto.co', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetAllSports data api"
    
    """
    url = f"https://sportapi1.p.rapidapi.com/api/sportsbook/getallsports"
    querystring = {}
    if referer:
        querystring['referer'] = referer
    if origin:
        querystring['Origin'] = origin
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportapi1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getliveevents(referer: str='https://fullreto.co/', origin: str='https://fullreto.co', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetLiveEvents Api Data"
    
    """
    url = f"https://sportapi1.p.rapidapi.com/api/sportsbook/getliveevents"
    querystring = {}
    if referer:
        querystring['Referer'] = referer
    if origin:
        querystring['Origin'] = origin
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportapi1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getfavouriteschamps(referer: str='https://fullreto.co/', origin: str='https://fullreto.co', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetFavouritesChamps Api Data"
    
    """
    url = f"https://sportapi1.p.rapidapi.com/api/sportsbook/getfavouriteschamps"
    querystring = {}
    if referer:
        querystring['referer'] = referer
    if origin:
        querystring['origin'] = origin
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportapi1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def gettopsportmenu(referer: str='https://fullreto.co/', origin: str='https://fullreto.co', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetTopSportMenu Api Data"
    
    """
    url = f"https://sportapi1.p.rapidapi.com/api/sportsbook/gettopsportmenu"
    querystring = {}
    if referer:
        querystring['Referer'] = referer
    if origin:
        querystring['origin'] = origin
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportapi1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def gethighlights(origin: str='https://fullreto.co', referer: str='https://fullreto.co/', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetHighlights Api Data"
    
    """
    url = f"https://sportapi1.p.rapidapi.com/api/sportsbook/gethighlights"
    querystring = {}
    if origin:
        querystring['origin'] = origin
    if referer:
        querystring['referer'] = referer
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportapi1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getlivenow(origin: str='https://fullreto.co', referer: str='https://fullreto.co/', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetLivenow Api Data"
    
    """
    url = f"https://sportapi1.p.rapidapi.com/api/sportsbook/getlivenow"
    querystring = {}
    if origin:
        querystring['Origin'] = origin
    if referer:
        querystring['referer'] = referer
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportapi1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getupcoming(origin: str='https://fullreto.co', referer: str='https://fullreto.co/', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GetUpcoming Api data"
    
    """
    url = f"https://sportapi1.p.rapidapi.com/api/sportsbook/getupcoming"
    querystring = {}
    if origin:
        querystring['origin'] = origin
    if referer:
        querystring['referer'] = referer
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportapi1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

