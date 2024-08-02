from dash import html
import dash_bootstrap_components as dbc
"""
    Renderiza cartões com informações sobre as criptomoedas.

    Parâmetros:
    df (DataFrame): O DataFrame contendo os dados das criptomoedas.
    crypto_icons (dict): Um dicionário contendo URLs dos ícones das criptomoedas.

    Retorna:
    list: Uma lista de cartões HTML contendo informações sobre as criptomoedas.
    """
def CryptoCards(df, crypto_icons):
    cards = []
    for _, row in df.iterrows():
        card = dbc.Card(
            dbc.CardBody([
                html.Img(src=crypto_icons[row['Criptomoeda']], style={'width': '50px', 'height': '50px'}),
                html.H3(row['Criptomoeda'], className='card-title'),
                html.H4(f'R${row["Preço Real 2"]}', className='card-text'),
                html.P(f'Variação: {row["Variação (%)"]}'),
                html.P(f'Última Atualização: {row["Última Atualização"]}')
            ]),
            style={'width': '18rem', 'margin': '10px'}
        )
        cards.append(card)
    return cards
