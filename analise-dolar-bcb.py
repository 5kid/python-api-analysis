import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def buscar_dados_dolar_ultimos_30_dias():
    """
    Busca na API do Banco Central a cotação do dólar dos últimos 30 dias.
    """
    print("Buscando dados na API do Banco Central...")

    data_final = datetime.now()
    data_inicial = data_final - timedelta(days=30)

    data_final_str = data_final.strftime('%m-%d-%Y')
    data_inicial_str = data_inicial.strftime('%m-%d-%Y')

    # URL CORRIGIDA:
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='{data_inicial_str}'&@dataFinalCotacao='{data_final_str}'&$format=json"

    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            print("Dados recebidos com sucesso!")
            dados = response.json()
            return dados['value']
        else:
            print(f"Erro ao buscar dados. Status: {response.status_code}")
            return None

    except Exception as e:
        print(f"Ocorreu um erro de conexão: {e}")
        return None

def analisar_e_plotar(dados):
    """
    Recebe os dados do BCB, usa Pandas para analisar e Matplotlib para plotar.
    """
    if dados is None or not dados:
        print("Não há dados para analisar.")
        return

    print("Analisando dados com Pandas...")
    df = pd.DataFrame(dados)

    df['dataHoraCotacao'] = pd.to_datetime(df['dataHoraCotacao'], errors='coerce')
    df['cotacaoCompra'] = pd.to_numeric(df['cotacaoCompra'], errors='coerce')
    df = df.dropna(subset=['dataHoraCotacao', 'cotacaoCompra'])
    df = df.sort_values(by='dataHoraCotacao')

    if df.empty:
        print("Não foi possível processar os dados (talvez seja fim de semana ou feriado e não houve cotação).")
        return

    print("Amostra dos dados analisados (5 primeiras linhas):")
    print(df.head())

    print("Gerando gráfico com Matplotlib...")
    plt.figure(figsize=(12, 6))
    plt.plot(df['dataHoraCotacao'], df['cotacaoCompra'], label='Cotação de Compra', marker='o', linestyle='-')
    plt.title('Variação do Dólar (USD) nos Últimos 30 Dias')
    plt.xlabel('Data')
    plt.ylabel('Valor (R$)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig('variacao_dolar.png')
    print("\nGráfico 'variacao_dolar.png' salvo com sucesso na sua pasta!")

if __name__ == "__main__":
    lista_de_cotacoes = buscar_dados_dolar_ultimos_30_dias()
    analisar_e_plotar(lista_de_cotacoes)
