import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def download_video_without_watermark(video_url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Download Video Without Watermark"
    
    """
    url = f"https://tiktok82.p.rapidapi.com/getdownloadvideowithoutwatermark"
    querystring = {'video_url': video_url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def download_video_with_watermark(video_url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Download Video With Watermark"
    
    """
    url = f"https://tiktok82.p.rapidapi.com/getdownloadvideowithwatermark"
    querystring = {'video_url': video_url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def music_id_by_url(url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get music id by url"
    
    """
    url = f"https://tiktok82.p.rapidapi.com/getmusicidbyurl"
    querystring = {'url': url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def video_id_by_url(url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get video Id by  url"
    
    """
    url = f"https://tiktok82.p.rapidapi.com/getvideoidbyurl"
    querystring = {'url': url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def challenge_videos(hashtag: str, cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get challenge videos by challenge _id"
    
    """
    url = f"https://tiktok82.p.rapidapi.com/getchallengevideos"
    querystring = {'hashtag': hashtag, }
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def music_info(music_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get music information by music_id"
    
    """
    url = f"https://tiktok82.p.rapidapi.com/getmusicinfo"
    querystring = {'music_id': music_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def video_comments(video_id: str, cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get video comments by video_id"
    
    """
    url = f"https://tiktok82.p.rapidapi.com/getvideocomments"
    querystring = {'video_id': video_id, }
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def challenge(hashtag: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get challenge by hashtag"
    
    """
    url = f"https://tiktok82.p.rapidapi.com/getchallenge"
    querystring = {'hashtag': hashtag, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def profile(username: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get profile information by username"
    
    """
    url = f"https://tiktok82.p.rapidapi.com/getprofile"
    querystring = {'username': username, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_videos(secuid: str, user_id: str, cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get user videos by user_id and  secUid"
    
    """
    url = f"https://tiktok82.p.rapidapi.com/getuservideos"
    querystring = {'secUid': secuid, 'user_id': user_id, }
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def video_comment_replies(comment_id: str, video_id: str, cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get video comment replies"
    
    """
    url = f"https://tiktok82.p.rapidapi.com/getvideocommentreplies"
    querystring = {'comment_id': comment_id, 'video_id': video_id, }
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def video_info(video_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get video information by video_id"
    
    """
    url = f"https://tiktok82.p.rapidapi.com/getvideoinfo"
    querystring = {'video_id': video_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def videos_by_music(music_id: str, cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get videos by music_id"
    
    """
    url = f"https://tiktok82.p.rapidapi.com/getvideosbymusic"
    querystring = {'music_id': music_id, }
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

