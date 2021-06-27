# MyTop10Songs

Esta aplicação tem o objetivo de obter as 10 músicas mais populares de um determinado artista através da API do [Genius](https://docs.genius.com/#/getting-started-h1) dando uma resposta no formato json na seguinte estrutura:

```
{
  "artist": "U2",
  "guess": "U2",
  "songs": [
    "One by U2",
    "With or Without You by U2",
    "Sunday Bloody Sunday by U2",
    "I Still Haven't Found What I'm Looking For by U2",
    "U2 by Ernia",
    "Pride (In the Name of Love) by U2",
    "Beautiful Day by U2",
    "Get Out of Your Own Way by U2 (Ft. Kendrick Lamar)",
    "​u21 by Mert (Ft. Samra)",
    "Where the Streets Have No Name by U2"
  ],
  "uuid": "56ba8f16-5ecc-49d6-bee5-c6ef7bfb3a08"
}
```

## Funcionalidades

- Obter as musicas através da API do Genius
- Salvar no DynamoDB (TinyDB)
- Salvar no Redis para criação de cache e com retenção de 7 dias

## Tecnologias e requerimentos

- Requer Python >= 3.6.9
- Requests para integração com Genius
- Fakeredis para simular e testar o redis
- Tinydb para persistência de dados
- Pytest para teste unitários
- Flask para criar a API

## Executando

Para executar a aplicação primeiramente precisamos baixar o repositório para nossa máquina local. Vamos clonar o repositório do projeto via HTTP para um diretório de escolha nossa:

`$ git clone https://github.com/drmcarvalho/mytop10songs.git`

Acessa o diretório do projeto usando o seguinte comando:

`$ cd mytop10songs`

Em seguida vamos instalar as depedencias executando o seguinte comando:

`$ pip install -r requirements.txt`

Apos instalado as depedencias, vamos iniciar a variavel de ambiente `FLASK_APP` para executar a aplicação flask:

`$ export FLASK_APP=app`

_Obs: você pode instalar as depedencias de forma global ou no virtualenv._

Habilite o modo de desenvolvimento e debug:

`export FLASK_ENV=development`

Feito isto basta iniciar o Flask:

`flask run`

## Consumindo a API

Esta aplicação possui um endpoint que tem a finalidade de fornecer as dez músicas mais populares de um determinado artista, o termo `q` é passado para o endpoint no formato de _querystring_ e é obrigatório.

## Songs

### GET /songs

`"q"  corresponde ao termo de busca`

Exemplo de requisição em cURL:

```
curl --request GET \
  --url 'http://127.0.0.1:5000/api/v1/songs?q=U2'
```

## Testes

O pytest é foi usado para facilitar nos testes unitários, para testar basta executar:

`pytest tests.py`

ou se dejesar ver as saídas

`pytest tests.py -s`
