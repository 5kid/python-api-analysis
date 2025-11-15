# Projeto 1: Análise de APIs e Redes com Python

Este repositório contém dois scripts Python que demonstram o consumo de APIs externas, a análise de dados e o monitoramento de rede, aplicando conceitos de engenharia de telecomunicações.

## O que este projeto prova?
* Fluência em **Python** para automação e análise.
* Uso de **Pandas** e **Matplotlib** para tratar e visualizar dados.
* Consumo de **APIs REST** (Banco Central, GitHub, Binance).
* Compreensão de **Camadas de Rede (Modelo OSI/TCP-IP)**:
    * **Camada 3 (Rede):** Monitoramento da latência com `ping` (protocolo ICMP).
    * **Camada 7 (Aplicação):** Monitoramento de status de API com `requests` (protocolo HTTP).

---

### Script 1: `analise_dolar_bcb.py`

Este script consome a API de dados abertos do Banco Central do Brasil para buscar o histórico de cotação do Dólar (USD) dos últimos 30 dias. Em seguida, utiliza **Pandas** para organizar os dados e **Matplotlib** para gerar e salvar um gráfico da variação.

**Como Usar:**
```bash
# 1. Instale as dependências (necessário apenas uma vez)
# pip install requests pandas matplotlib

# 2. Rode o script
python3 analise_dolar_bcb.py
