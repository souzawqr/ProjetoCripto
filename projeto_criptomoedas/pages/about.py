from dash import dcc, html
import dash_bootstrap_components as dbc

def aboutpage():
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
            brand="Dashboard de Criptomoedas",
            brand_href="/",
            color="dark",
            dark=True,
            className="mb-4"
        ),
        dbc.Container([
            dbc.Row([
                dbc.Col(html.H1("Sobre Nós", className="text-center mt-4"))
            ]),
            dbc.Row([
                dbc.Col(html.P("Este é um dashboard para acompanhar os preços das principais criptomoedas. Atualizamos os preços a cada minuto e oferecemos uma visualização clara e fácil de entender dos dados mais recentes.", className="text-center mt-4"))
            ]),
            dbc.Row([
                dbc.Col(html.P("Nossa missão é fornecer informações precisas e atualizadas sobre criptomoedas para ajudar você a tomar decisões informadas.", className="text-center mt-2"))
            ]),
            dbc.Row([
                dbc.Col(html.H2("Por que escolher o nosso dashboard?", className="text-center mt-4"))
            ]),
            dbc.Row([
                dbc.Col([
                    html.H3("Interface Intuitiva", className="text-center"),
                    html.P("Nosso dashboard foi projetado com uma interface intuitiva e fácil de usar, para que você possa acompanhar os preços das criptomoedas sem complicações.", className="text-center")
                ], width=4),
                dbc.Col([
                    html.H3("Dados Atualizados", className="text-center"),
                    html.P("Atualizamos os preços das criptomoedas a cada minuto, garantindo que você tenha acesso às informações mais recentes.", className="text-center")
                ], width=4),
                dbc.Col([
                    html.H3("Personalização", className="text-center"),
                    html.P("Você pode personalizar o dashboard selecionando quais criptomoedas deseja acompanhar, adaptando-o às suas necessidades específicas.", className="text-center")
                ], width=4)
            ]),
            dbc.Row([
                dbc.Col(html.H2("Quem somos nós?", className="text-center mt-4"))
            ]),
            dbc.Row([
                dbc.Col([
                    html.Img(src="/assets/team.jpg", className="img-fluid rounded-circle mx-auto d-block", width="200"),
                    html.H3("Equipe de Desenvolvimento", className="text-center mt-2"),
                    html.P("Nossa equipe é formada por André Oliveira , Rodrigo Souza, Rodrigo Gonsalves, Laércio Rodrigues  e Felipe Barbosa - especialistas em desenvolvimento web e análise de dados, dedicados a fornecer a você a melhor experiência possível com nosso dashboard.", className="text-center")
                ])
            ])
        ], fluid=True)
    ])
