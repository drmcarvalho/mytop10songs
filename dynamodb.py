from tinydb import TinyDB, Query

# collection = TinyDB('collection.json')
collection = None


def init(nameCollection):
    global collection
    collection = TinyDB(nameCollection)


def insert(document):
    collection.insert(document)


def search(query):
    return collection.search(query)
