 Sistema de Planejamento de Demanda de Fardamento em Centro de Distribuição de Uniformes - API Analítica


# Descrição

Esta API é responsável pelo processamento de dados e cálculo de previsão de demanda com base no histórico de consumo.

Ela atua como um módulo independente dentro da arquitetura de microsserviços, sendo consumida pela API principal.


# Arquitetura

API Principal → API Analítica → Processamento de Dados


# Tecnologias utilizadas

- Python
- FastAPI
- Docker


# Funcionalidades

- Cálculo de média de consumo
- Previsão de demanda
- Sugestão de reposição
- Identificação de itens críticos


# Rotas

- GET /health → verificação de funcionamento
- POST /previsao → cálculo de previsão
- POST /classificacao → classificação ABC
- POST /reposicao → sugestão de reposição
- POST /criticos → identificação de itens críticos


# Instalação e execução

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001


# Acesso

http://127.0.0.1:8001/docs


# Docker

docker build -t api-analitica
docker run -p 8001:8001 api-analitica

boas práticas de separação backend/frontend,

documentação com OpenAPI (Swagger),

uso de diferentes rotas (GET, POST, DELETE).
