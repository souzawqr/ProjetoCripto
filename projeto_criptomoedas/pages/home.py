# pages/home.py

from dash import dcc, html
import dash_bootstrap_components as dbc
from components.crypto_graph import CryptoGraph
from components.crypto_cards import CryptoCards
from components.download_button import DownloadButton
from config import crypto_urls  # Importa crypto_urls do config.py

def homepage():
    return dbc.Container([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dcc.Link("Home", href="/", className="nav-link")),
                dbc.NavItem(dcc.Link("Sobre", href="/sobre", className="nav-link")),
                dbc.NavItem(dbc.NavLink("Transfero", href="https://transfero.com/", target="_blank")),
                dbc.NavItem(dbc.NavLink("Instagram", href="https://www.instagram.com/senac_rj/", target="_blank")),
                dbc.NavItem(dbc.NavLink("WhatsApp", href="https://web.whatsapp.com/send?text=Confira os preços das criptomoedas no nosso dashboard!", target="_blank")),
                dbc.NavItem(dbc.NavLink("Enviar por E-mail", href="mailto:?subject=Preços das Criptomoedas&body=Confira os preços das criptomoedas no nosso dashboard!", target="_blank"))
            ],
            brand="Projeto Senac & Transfero Criptomoedas",
            brand_href="/",
            color="dark",
            dark=True,
            className="mb-4"
        ),
        dcc.Interval(id='interval-component', interval=60*1000, n_intervals=0),  # Atualização a cada 1 minuto
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(
                    id='crypto-filter',
                    options=[{'label': key, 'value': key} for key in crypto_urls.keys()],
                    multi=True,
                    placeholder="Selecione as Criptomoedas",
                ),
            ], width=12, className="mb-4")
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='crypto-graph'),
            ], width=12)
        ]),
        dbc.Row([
            dbc.Col([
                html.Div(id='crypto-prices', style={'marginTop': '20px', 'display': 'flex', 'flexWrap': 'nowrap', 'overflowX': 'auto'})
            ], width=12)
        ]),
        dbc.Row([
            dbc.Col([
                html.Div(id='crypto-details')
            ], width=12)
        ]),
        dbc.Row([
            dbc.Col([
                DownloadButton(),
            ], width=12, className="d-flex justify-content-center")
        ])
    ], fluid=True)
