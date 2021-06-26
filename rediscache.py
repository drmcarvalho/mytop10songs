import fakeredis
import time

ONE_WEEK = 86400  # Retencao de 7 dias

server = fakeredis.FakeServer()
r = fakeredis.FakeStrictRedis(server=server)


def getCache(name):
    return r.get(name)


def setCache(name, content, timeExpire=ONE_WEEK):
    r.pexpire(name, timeExpire)
    r.hset(name, mapping=content)


def setCacheList(name, values, timeExpire=ONE_WEEK):
    r.pexpire(name, timeExpire)
    r.lpush(name, values)


def deleteCache(name):
    r.delete(name)


def addCache(name, value):
    r.expire(name, ONE_WEEK)
    r.set(name, value)


def cache(name):
    return r.get(name)
