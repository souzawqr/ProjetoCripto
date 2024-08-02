import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash import html

def Navbar():
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dcc.Link("Home", href="/", className="nav-link")),
            dbc.NavItem(dcc.Link("Sobre", href="/sobre", className="nav-link")),
            dbc.NavItem(dbc.NavLink("Transfero", href="https://transfero.com/", target="_blank")),
            dbc.NavItem(dbc.NavLink("Instagram", href="https://www.instagram.com/senac_rj/", target="_blank")),
            dbc.NavItem(dbc.NavLink("WhatsApp", href="https://web.whatsapp.com/send?text=Confira os preços das criptomoedas no nosso dashboard!", target="_blank")),
            dbc.NavItem(dbc.NavLink("Enviar por E-mail", href="mailto:?subject=Preços das Criptomoedas&body=Confira os preços das criptomoedas no nosso dashboard!", target="_blank"))
        ],
        brand="Projeto Transfero & Senac Criptomoedas",
        brand_href="/",
        color="dark",
        dark=True,
        className="mb-4"
    )
