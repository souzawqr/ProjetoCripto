import dash_bootstrap_components as dbc
from dash import dcc

def DownloadButton():
    return dbc.Button("Baixar dados como CSV", id="download-btn", color="primary", className="mt-4")

def DownloadComponent():
    return dcc.Download(id="download-dataframe-csv")
