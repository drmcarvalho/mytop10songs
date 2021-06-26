from flask import Flask, jsonify, request
from tinydb import Query
import util
import dynamodb
import genius
import rediscache


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

dynamodb.init('collection.json')


def formatResponse(guess, artist, songs, uuid):
    """
    Decodifica a string em bytes liteal em utf-8 e monta o corpo da resposta da API.
    :param guess: termo para a busca.
    :param artist: nome do artista.
    :param songs: lista de musicas.
    :param uuid: uuid versao 4.
    :return: dict contento o corpo da resposta HTTP.
    """
    songsDecode = []
    if isinstance(artist, bytes):
        artist = artist.decode('utf-8')
    if isinstance(uuid,  bytes):
        uuid = uuid.decode('utf-8')
    for song in songs:
        if isinstance(song, bytes):
            song = song.decode('utf-8')
            songsDecode.append(song)
    return {'guess': guess, 'artist': artist, 'songs': songsDecode if len(songsDecode) > 0 else songs, 'uuid': uuid}


def addSongsCache(data, name):
    for i, item in enumerate(data):
        rediscache.addCache(f's{i+1}-{name}', item)


def addUUIDCache(uuid, name):
    rediscache.addCache(f'uuid-{name}', uuid)


def getSongsCache(name):
    songs = []
    for i in range(0, 10):
        item = rediscache.cache(f's{i+1}-{name}')
        if item:
            songs.append(item)
    return songs if len(songs) > 0 else None


def addArtistCache(artist, guess):
    rediscache.addCache(f'artist-{guess}', artist)


def getArtistCache(guess):
    return rediscache.getCache(f'artist-{guess}')


def getFromDynamo(guess):
    Artist = Query()
    return dynamodb.search(Artist.guess == guess)


def requestAction(q, cache):
    if cache:
        songs = getSongsCache(q)
        artist = getArtistCache(q)
        uuid = rediscache.getCache(f'uuid-{q}')
        if songs:
            responseWithCache = formatResponse(q, artist, songs, uuid)
            return responseWithCache
    fromDynamo = getFromDynamo(q)
    if fromDynamo:
        addSongsCache(fromDynamo[0]['songs'], q)
        addArtistCache(fromDynamo[0]['artist'], q)
        addUUIDCache(fromDynamo[0]['uuid'], q)
        return fromDynamo[0]
    response = genius.search(q)
    artist = genius.getArtist(response)
    newUuid = util.uuidV4()
    responseFormatted = formatResponse(q, artist, genius.songs(response), newUuid)
    dynamodb.insert(responseFormatted)
    '''withCache = rediscache.getCache(q)
    if withCache:
        rediscache.deleteCache(q)'''
    addSongsCache(responseFormatted['songs'], q)
    addArtistCache(responseFormatted['artist'], q)
    addUUIDCache(newUuid, q)
    return responseFormatted


@app.route('/api/v1/song')
def song():
    q = request.args.get('q')
    withCache = request.args.get('cache', default='1').lower()
    if not q:
        return jsonify({'error': 'parameter f was not specified'}), 200
    if withCache == 'true' or withCache == '1':
        return jsonify(requestAction(q, True)), 200
    return jsonify(requestAction(q, False)), 200


if __name__ == '__main__':
    app.run()
