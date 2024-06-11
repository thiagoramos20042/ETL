import yfinance as yf
import pandas as pd
from loguru import logger
import time

start_time = time.time()
commodities = ['CL=F', 'GC=F', 'SI=F']  # Petróleo bruto, Ouro, Prata

# Adiciona o log com nível de informação
logger.add("file_{time}.log", level="INFO")

def buscar_dados_commodities(simbolo, periodo='5d', intervalo='1d'):
    """
    Recebe um parâmetro e retorna o preço dessas ações.
    """
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period=periodo, interval=intervalo)
    dados['simbolo'] = simbolo  # Adiciona a coluna do símbolo
    logger.info(f"Dados de {simbolo}: {dados}")
    return dados
    
def buscar_todos_dados_commodities(commodities):
    """
    Concatena todos os preços de ações.
    """
    todos_dados = []
    for simbolo in commodities:
        dados_de_commodities = buscar_dados_commodities(simbolo)
        todos_dados.append(dados_de_commodities)
        logger.info(f"Dados concatenados para {simbolo}: {dados_de_commodities}")
    return pd.concat(todos_dados)

if __name__ == "__main__":
    dados_de_todas_as_commodities = buscar_todos_dados_commodities(commodities)
    logger.info(f"Dados de todas as commodities: {dados_de_todas_as_commodities}")
    logger.info(f"Tempo total de execução: {time.time() - start_time} segundos")
