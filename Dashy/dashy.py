'''
Module responsible for defining the dashboard layout and styling. 
'''
import dash
import dash_bootstrap_components as dbc
from dash import html

from Dashy.analysis import country_count_df
from Dashy.components import (bar_component, map_component, navbar,
                              pie_component)


dash_app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server = dash_app.server 


borders = [0 for _ in range(len(country_count_df))],

dash_row1 = dbc.Row([dbc.Col(map_component, md=12)])
dash_row2 = dbc.Row([
    dbc.Col(bar_component, md=6),
    dbc.Col(pie_component, md=6)
])

dash_app.layout = html.Div([    
    navbar,
    html.Br(),
    dash_row1,
    html.Br(),
    dash_row2,
],

    style={'backgroundColor': 'black'}
)
