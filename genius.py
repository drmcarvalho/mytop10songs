import requests


TOKEN = '15wkAF8IJKq621Qrvjr8zXIjBx_1Qs5rdUCiC5nvJpTA_QAcShPhymvusPGV6vKD'  # env
API = 'https://api.genius.com'
RESOURCE_SEARCH = '/search?q='
AUTH = {'Authorization': f'Bearer {TOKEN}'}


def search(q):
    if not q:
        raise ValueError(q)
    response = requests.get(API + RESOURCE_SEARCH + q, headers=AUTH)
    return response.json()


def formatStr(s):
    return s.replace(u'\xa0', u' ').strip()


def songs(data):
    songs = [formatStr(song['result']['full_title']) for song in data['response']['hits']]
    return songs


def getArtist(data):
    artist = [formatStr(song['result']['primary_artist']['name']) for song in data['response']['hits']]
    if len(artist) > 0:
        return artist[0]
    return None
