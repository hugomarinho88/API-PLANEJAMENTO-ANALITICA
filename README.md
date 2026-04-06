# API de Fardamento da Marinha

API REST desenvolvida em Python com Flask para controle simples de itens de fardamento
do Centro de Distribuição de Uniformes da Base de Abastecimento da Marinha no Rio de Janeiro.

## Tecnologias utilizadas

- Python
- Flask
- SQLite
- Flasgger (Swagger / OpenAPI)
- Flask-CORS

## Funcionalidades

- Cadastro de itens de fardamento (tipo, tamanho, quantidade, setor)
- Listagem de todos os itens cadastrados
- Consulta de item por ID
- Exclusão de item por ID
- Documentação automática da API com Swagger

## Estrutura principal das rotas

- `GET /`  
  Verifica se a API está no ar.

- `GET /fardamentos`  
  Lista todos os itens de fardamento.

- `POST /fardamentos`  
  Cadastra um novo item de fardamento.

- `GET /fardamentos/<id>`  
  Consulta um item específico pelo ID.

- `DELETE /fardamentos/<id>`  
  Remove um item específico pelo ID.

## Banco de dados

É utilizado um banco SQLite chamado `fardamento.db`.  
A tabela principal é:

```sql
CREATE TABLE fardamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    tamanho TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    setor TEXT
);


git clone <URL_DO_REPOSITORIO_BACKEND>
cd backend-api
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py


A API ficará disponível em:

http://127.0.0.1:5000/ – página inicial

http://127.0.0.1:5000/apidocs – documentação Swagger

Demonstra-se:

uso de Flask e SQLite,

boas práticas de separação backend/frontend,

documentação com OpenAPI (Swagger),

uso de diferentes rotas (GET, POST, DELETE).