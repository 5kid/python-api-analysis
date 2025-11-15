import requests
import ping3
import time

# (Nome do Serviço, URL da API para testar, Domínio para Pingar)
SERVICOS_PARA_CHECAR = [
    ("GitHub", "https://api.github.com", "api.github.com"),
    ("Binance", "https://api.binance.com/api/v3/ping", "api.binance.com"),
    ("Google DNS", "https://dns.google/resolve?name=google.com", "8.8.8.8"),
    ("API Falsa (Erro)", "https://api.servicoquenaoexiste.com", "servicoquenaoexiste.com")
]

def monitorar_servicos(lista_de_servicos):
    """
    Passa pela lista de serviços, checando Camada 3 (Ping) e Camada 7 (API).
    """
    print("Iniciando Monitoramento de Rede e Aplicação...")
    print("-" * 60)

    for nome, url, dominio in lista_de_servicos:
        print(f"Checando Serviço: {nome}")

        # --- TESTE DE CAMADA 3 (REDE) ---
        try:
            latencia_ms = ping3.ping(dominio, unit='ms', timeout=2)

            if latencia_ms is False:
                print(f"  [Camada 3 - Rede]: FALHA. Host '{dominio}' não respondeu ao ping (timeout).")
            elif latencia_ms is None:
                print(f"  [Camada 3 - Rede]: FALHA. Host '{dominio}' desconhecido ou inalcançável.")
            else:
                print(f"  [Camada 3 - Rede]: SUCESSO. Latência (Ping): {latencia_ms:.2f} ms")

        except Exception as e:
            print(f"  [Camada 3 - Rede]: ERRO. Falha ao executar o ping para '{dominio}': {e}")

        # --- TESTE DE CAMADA 7 (APLICAÇÃO) ---
        try:
            start_time = time.time()
            response = requests.get(url, timeout=5)
            response_time = (time.time() - start_time) * 1000 # em milissegundos

            if 200 <= response.status_code < 300:
                print(f"  [Camada 7 - API]: SUCESSO. Status: {response.status_code}. Tempo: {response_time:.2f} ms")
            else:
                print(f"  [Camada 7 - API]: FALHA. Aplicação respondeu com erro. Status: {response.status_code}")

        except requests.exceptions.Timeout:
            print(f"  [Camada 7 - API]: FALHA. A requisição para '{url}' demorou demais (Timeout).")
        except requests.exceptions.RequestException:
            print(f"  [Camada 7 - API]: FALHA. Não foi possível conectar na API em '{url}'.")

        print("-" * 60)

if __name__ == "__main__":
    ping3.EXCEPTIONS = True
    monitorar_servicos(SERVICOS_PARA_CHECAR)
