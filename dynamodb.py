from tinydb import TinyDB, Query


collection = None


def init(nameCollection):
    """
    Inicializacao do banco de dados.
    :param nameCollection: nome do arquivo representante da collection.
    """
    global collection
    collection = TinyDB(nameCollection)


def insert(document):
    """
    Insercao de um novo documento no banco de dados.
    :param document: documento em formato json.
    """
    collection.insert(document)


def search(query):
    """
    Efetua uma busca no banco de dados.
    :param query: e uma instancia da classe Query do TinyDB onde podemos efetuar busca com condicoes
    :return: dict de uma collection que satisfaca a condicao de pesquisa.
    """
    return collection.search(query)
