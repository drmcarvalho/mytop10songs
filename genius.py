import requests


TOKEN = '15wkAF8IJKq621Qrvjr8zXIjBx_1Qs5rdUCiC5nvJpTA_QAcShPhymvusPGV6vKD'  # env
API = 'https://api.genius.com'
RESOURCE_SEARCH = '/search?q='
AUTH = {'Authorization': f'Bearer {TOKEN}'}


def search(q):
    """
    Faz uma busca para o endpoint /search da API do Genius usando o q como query string.
    :param q: termo para busca
    :return: dict com conteudo da resposta da API do Genius
    """
    if not q:
        raise ValueError(q)
    response = requests.get(API + RESOURCE_SEARCH + q, headers=AUTH)
    return response.json()


def formatStr(s):
    """
    Tratamento de espaço e outros caracteres na string.
    :param s: valor do campo para ser tratado
    :return: str com caracteres tratados e sem espaços desnecessarios
    """
    return s.replace(u'\xa0', u' ').strip()


def songs(data):
    """
    Extração das musicas.
    :param data: dict com os dados da API do Genius
    :return: list com os nomes das musicas
    """
    return [formatStr(song['result']['full_title']) for song in data['response']['hits']]


def getArtist(data):
    """
    Extracao dos nomes dos artistas
    :param data: dict com os dados da API do Genius
    :return: str contendo o nome do artista pesquisado
    """
    artist = [formatStr(song['result']['primary_artist']['name']) for song in data['response']['hits']]
    if len(artist) > 0:
        return artist[0]
    return None
