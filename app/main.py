from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="API Secundária - Estudo de Demanda de Fardamento",
    description="Executa cálculos de previsão, criticidade e reposição.",
    version="1.0.0"
)


class PrevisaoRequest(BaseModel):
    item: str
    historico: list[int]
    estoque_atual: int
    estoque_minimo: int


@app.get("/")
def root():
    return {"mensagem": "API Analítica em funcionamento"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/previsao")
def calcular_previsao(dados: PrevisaoRequest):
    media = sum(dados.historico) / len(dados.historico)
    previsao_proximo_mes = round(media)

    sugestao_reposicao = max(0, (previsao_proximo_mes + dados.estoque_minimo) - dados.estoque_atual)

    status = "adequado"
    if dados.estoque_atual < dados.estoque_minimo:
        status = "crítico"
    elif dados.estoque_atual < previsao_proximo_mes:
        status = "atenção"

    return {
        "item": dados.item,
        "media_historica": media,
        "previsao_proximo_mes": previsao_proximo_mes,
        "estoque_atual": dados.estoque_atual,
        "estoque_minimo": dados.estoque_minimo,
        "sugestao_reposicao": sugestao_reposicao,
        "status_estoque": status
    }


@app.post("/classificacao")
def classificar_item(dados: PrevisaoRequest):
    total = sum(dados.historico)

    if total >= 100:
        classe = "A"
    elif total >= 50:
        classe = "B"
    else:
        classe = "C"

    return {
        "item": dados.item,
        "consumo_total": total,
        "classificacao": classe
    }


@app.post("/reposicao")
def calcular_reposicao(dados: PrevisaoRequest):
    media = sum(dados.historico) / len(dados.historico)
    reposicao = max(0, round((media * 2) + dados.estoque_minimo - dados.estoque_atual))

    return {
        "item": dados.item,
        "reposicao_sugerida": reposicao
    }


@app.post("/criticos")
def verificar_critico(dados: PrevisaoRequest):
    media = sum(dados.historico) / len(dados.historico)

    return {
        "item": dados.item,
        "critico": dados.estoque_atual < media
    }