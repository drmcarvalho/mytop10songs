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
    "\u200bu21 by Mert (Ft. Samra)", 
    "Where the Streets Have No Name by U2"
  ], 
  "uuid": "11b561d6-33bc-4ba8-b3e3-b801562d3d0c"
}
```

## Funcionalidades

- Obter as musicas através da API do Genius
- Salvar no DynamoDB (TinyDB)
- Salvar no Redis para criação de cache e com retenção de 7 dias

## Tecnologias 

- Requer Python >= 3.6.9
- Requests para integração com Genius
- Fakeredis para simular e testar o redis
- Tinydb para persistência de dados
- Pytest para teste unitários
- Flask para criar a API


