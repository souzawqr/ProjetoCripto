import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
import requests
from bs4 import BeautifulSoup
import dash_bootstrap_components as dbc
from datetime import datetime
from pages.home import homepage
from pages.about import aboutpage
from components.crypto_cards import CryptoCards
from components.download_button import DownloadButton, DownloadComponent

# Função para obter os preços e a variação das criptomoedas
def get_crypto_price(url):
    link_dollar = 'https://www.google.com/search?q=dollar+to+real'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    requisicao_cripto = requests.get(url, headers=headers)
    requisicao_dollar = requests.get(link_dollar, headers=headers)
    site = BeautifulSoup(requisicao_cripto.text, 'html.parser')
    site_2 = BeautifulSoup(requisicao_dollar.text, 'html.parser')
    
    precoUm = site.find('div', class_='css-1bwgsh3')
    variação_tag = site.find('td', {'data-bn-type': 'text', 'class': 'css-1604ved'})
    if variação_tag:
        variação = variação_tag.get_text()
    else:
        variação = 'N/A'
    
    dollar = site_2.find('span', class_='SwHCTb').get_text()
    
    pLimpo = precoUm.get_text().replace('$', '').replace(' ', '').replace(',', '')
    dollarLimpo = float(dollar.replace(',', '.'))
    real = float(pLimpo)
    preco_real = real * dollarLimpo
    preco_real_2 = f'{preco_real:_.2f}'
    preco_real_2 = preco_real_2.replace('.', ',').replace('_', '.')

    return preco_real, variação, preco_real_2

# URLs das criptomoedas
crypto_urls = {
    'Bitcoin': 'https://www.binance.com/pt-BR/price/bitcoin',
    'Ethereum': 'https://www.binance.com/pt-BR/price/ethereum',   
    'Monero': 'https://www.binance.com/pt-BR/price/monero',
    'Solana': 'https://www.binance.com/pt-BR/price/solana',
    'Dogecoin': 'https://www.binance.com/pt-BR/price/dogecoin',
    'Renzo': 'https://www.binance.com/pt-BR/price/renzo',
}


# Obtendo os preços das criptomoedas
def obter_dados():
    criptomoedas = []
    for crypto, url in crypto_urls.items():
        preco_em_real, variação, preço_real_2 = get_crypto_price(url)
        criptomoedas.append((crypto, preco_em_real, variação, preço_real_2))
    df = pd.DataFrame(criptomoedas, columns=['Criptomoeda', 'Preço em Real', 'Variação (%)', 'Preço Real 2'])
    df['Última Atualização'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    return df

# Inicializando o aplicativo Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
app.title = "Projeto Senac & Transfero Criptomoedas"

# Ícones das criptomoedas
crypto_icons = {
    'Bitcoin': 'https://cryptologos.cc/logos/bitcoin-btc-logo.png?v=010',
    'Ethereum': 'https://cryptologos.cc/logos/ethereum-eth-logo.png?v=010',   
    'Monero': 'https://cryptologos.cc/logos/monero-xmr-logo.png?v=002',
    'Solana': 'https://cryptologos.cc/logos/solana-sol-logo.png?v=010',
    'Dogecoin': 'https://cryptologos.cc/logos/dogecoin-doge-logo.png?v=002',
    'Renzo': 'https://cryptologos.cc/logos/ren-ren-logo.svg?v=032',    
}

# Callback para atualizar o gráfico e os preços
@app.callback(
    [Output('crypto-graph', 'figure'), Output('crypto-prices', 'children')],
    [Input('interval-component', 'n_intervals'), Input('crypto-filter', 'value')]
)
def update_dashboard(n, selected_cryptos):
    df = obter_dados()
    
    if selected_cryptos:
        df = df[df['Criptomoeda'].isin(selected_cryptos)]
    
    # Atualização do gráfico
    figure = {
        'data': [
            {'x': df['Criptomoeda'], 'y': df['Preço em Real'], 'type': 'bar', 'name': 'Preço em Real',
             'marker': {'color': ['#FFD700', '#6A5ACD', '#00CED1']}}
        ],
        'layout': {
            'title': 'Preços das Criptomoedas',
            'xaxis': {'title': 'Criptomoeda'},
            'yaxis': {'title': 'Preço em Real'},
            'plot_bgcolor': '#f8f9fa',
            'paper_bgcolor': '#f8f9fa'
        }
    }

    # Atualização dos preços
    price_cards = CryptoCards(df, crypto_icons)
    
    return figure, price_cards

# Callback para download do dataframe como CSV
@app.callback(
    Output("download-dataframe-csv", "data"),
    [Input("download-btn", "n_clicks")],
    prevent_initial_call=True,
)
def download_csv(n_clicks):
    df = obter_dados()
    return dcc.send_data_frame(df.to_csv, "crypto_data.csv")

# Callback para a navegação entre páginas
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/sobre':
        return aboutpage()
    else:
        return homepage()

# Layout da aplicação
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    DownloadComponent()  # Adiciona o componente de download
])

if __name__ == '__main__':
    app.run_server(debug=True)
