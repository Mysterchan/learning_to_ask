import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def getteams(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Obtener el listado de equipos de fútbol televisados en España."
    
    """
    url = f"https://wosti-futbol-tv-spain.p.rapidapi.com/api/teams"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "wosti-futbol-tv-spain.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getcompetitionsid(is_id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Obtener competición por identificador único del listado de competiciones de partidos de fútbol televisados en España.
		
		> Este endpoints requiere de un parámetro denominado Id."
    
    """
    url = f"https://wosti-futbol-tv-spain.p.rapidapi.com/api/competitions"
    querystring = {'Id': is_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "wosti-futbol-tv-spain.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def geteventsid(is_id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Obtener el evento por identificador único  del listado de eventos de partidos de fútbol televisados en España.
		
		> Este endpoints requiere de un parámetro denominado Id."
    
    """
    url = f"https://wosti-futbol-tv-spain.p.rapidapi.com/api/events"
    querystring = {'Id': is_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "wosti-futbol-tv-spain.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getevents(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Obtener el listado de eventos de partidos de fútbol televisados en España.
		
		> Este endpoints no requiere de ningún parámetro."
    
    """
    url = f"https://wosti-futbol-tv-spain.p.rapidapi.com/api/events"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "wosti-futbol-tv-spain.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getcompetitions(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Obtener el listado de competiciones de partidos de fútbol televisados en España.
		
		> Este endpoints no requiere de ningún parámetro."
    
    """
    url = f"https://wosti-futbol-tv-spain.p.rapidapi.com/api/competitions"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "wosti-futbol-tv-spain.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

