
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Função para obter os preços e a variação das criptomoedas
def get_crypto_price(url):
    link_dollar = 'https://www.google.com/search?q=dollar+to+real'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    requisicao_cripto = requests.get(url, headers=headers)
    requisicao_dollar = requests.get(link_dollar, headers=headers)
    site = BeautifulSoup(requisicao_cripto.text, 'html.parser')
    site_2 = BeautifulSoup(requisicao_dollar.text, 'html.parser')
    
    precoUm = site.find('div', class_='css-1bwgsh3')
    variação = site.find('td', {'data-bn-type': 'text', 'class': 'css-1604ved'}).get_text()
    
    dollar = site_2.find('span', class_='SwHCTb').get_text()
    
    pLimpo = precoUm.get_text().replace('$', '').replace(' ', '').replace(',', '')
    dollarLimpo = float(dollar.replace(',', '.'))
    real = float(pLimpo)
    preco_real = real * dollarLimpo

    return preco_real, variação

# URLs das criptomoedas
crypto_urls = {
    'Bitcoin': 'https://www.binance.com/pt-BR/price/bitcoin',
    'Ethereum': 'https://www.binance.com/pt-BR/price/ethereum',
    'Solana': 'https://www.binance.com/pt-BR/price/solana',
}

# Obtendo os preços das criptomoedas
def obter_dados():
    criptomoedas = []
    for crypto, url in crypto_urls.items():
        preco_em_real, variação = get_crypto_price(url)
        criptomoedas.append((crypto, preco_em_real, variação))
    df = pd.DataFrame(criptomoedas, columns=['Criptomoeda', 'Preço em Real', 'Variação (%)'])
    df['Última Atualização'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    return df
