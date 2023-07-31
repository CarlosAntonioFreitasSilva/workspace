# Backend com Python

Para desenvolver a aplicação backend vamos utilizar o FastAPI que é um framework web para construção de aplicações Python baseado em padrões abertos
 - OpenAPI para criações de API, incluindo declarações de operações de rota, parâmetros, corpo de requisições
 - Modelo de dados com JSON Schema

Para instalar o FastAPI utilizamos no prompt de comando, do sistema operacional

`pip install fastapi[all]`


Comentários:
- Existem outros frameworks tais como Roadmap e Django para desenvolver aplicações python.
- No PHP existe o framework Lavarel que utiliza o padrão de operações de rota

## App OlaMundo
Crie o arquivo `main.py` para implementarmos o código.

### Importando FastAPI

~~~python
from fastapi import FastAPI
~~~

### Criando instância

Criamos uma instância da classe `FastAPI` e armazenamos numa variável no qual chamaremos de `app`

~~~python
from fastapi import FastAPI

app = FastAPI()
~~~

### Criando operações de rotas

Uma rota é a última parta da URL que começa a partir de `/`

As operações de métodos HTTP
- `GET`
- `POST`
- `PUT`
- `DELETE`

Vamos criar uma operação `GET` cuja rota é `/`

~~~python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Olá, mundo"}
~~~

Ao acessar a rota `/` usando operação `GET` teremos como retorno o `dict`. 

Podemos retornar `list` e outros tipos de dados como `string`, `int`, modelos `Pydantic` e etc.

Para retornar HTML devemos importar `HTMLResponse` e adicionamos o parâmetro `response_class=HTMLResponse` na operação `GET`. Para exemplificar, vamos criar um rota `/html` que retorna uma página HTML. 

~~~python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get('/')
def root():
    return {"message": "Olá, mundo"}

@app.get('/html', response_class=HTMLResponse)
def root():
    return """
    <html lang="pt-br">
        <head>
            <title>APP Hello</title>
        </head>
        <body>
            <h1>Olá, mundo!</h1>
            <p>Esta é minha primeira página HTML</p>
        </body>
    </html>
~~~

### Executando o código

Para executar o código acessamos o diretório do arquivo onde está a nossa aplicação, nesse caso, o arquivo `main.py` e digitamos o comando para iniciarmos o servidor

`uvicorn main:app --reload`

Observe que foi utilizado o nome do arquivo `main` e nome da variável que armazena a instância da classe `FastAPI` que é `app`.

Após o servidor ter sido inicializado acesse


- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/html`

## Parâmetros de rotas

~~~python
@app.get("/ola")
def root(nome):
    return "Olá " + nome.capitalize()
~~~

O método `capitalize()` foi utilizado para a primeira letra do nome ficar maiúscula.

Para passar parâmetros pelo URL utilizamos `URL/ola/?nome=arg`. No nosso caso acessamos
`http://127.0.0.1:8000/ola/?nome=carlos`


Parei de estudar em https://fastapi.tiangolo.com/tutorial/query-params/