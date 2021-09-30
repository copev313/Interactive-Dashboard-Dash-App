'''
Module to hold the different graph components that will be featured in the
dashboard.
'''
from dash import dcc
import dash_bootstrap_components as dbc
from Dashy.analysis import (country_count_df, top_ten_df, 
                            restaurant_counts_df)
import plotly.graph_objs as go


# Navbar -- 
navbar = dbc.Nav()


# Map Graph Component --
map_component = dcc.Graph(
            id='8',
            figure = {
                'data': [{
                    'locations': country_count_df['country_code'],
                    'z': country_count_df['count'],
                    'colorscale': 'Earth',
                    'reversescale': True,
                    'hover-name': country_count_df['country_code'],
                    'type': 'choropleth',
                }],

                'layout': {
                    'title': dict(
                        text= 'Restaurant Frequency by Location',
                        font= dict(size=20, color='white')
                    ),
                    'paper_bgcolor': '#111111',
                    'plot_bgcolor': '#111111',
                    'height': 800,
                    'geo': dict(
                        bgcolor='rgba(0, 0, 0, 0)'
                    )
                }
            }
)


# Bar Graph Component --
bar_component =  dcc.Graph(
    id='bar1',
    figure={
        'data': [
            go.Bar( x=top_ten_df['Restaurant Name'],
                    y=top_ten_df['Votes'])
        ],

        'layout': {
            'title': dict(
                text='Top Restaurants in India',
                font=dict(size=20, color='white')
            ),
            'paper_bgcolor': '#111111',
            'plot_bgcolor': "#111111",
            'height': 600,

            'line': dict(
                color='white',
                width=4,
                dash='dash',
            ),

            'xaxis' : dict(
                tickfont=dict(color='white'),
                showgrid=False,
                title='',
                color='white'
            ),

            'yaxis' : dict(
                tickfont=dict(color='white'),
                showgrid=False,
                title='Number of Votes',
                color='white'
            )
        }
    }
)


# Pie Graph Component --
pie_component = dcc.Graph(
        id = 'pie3',
        figure = {
            'data': [
                {
                'labels': restaurant_counts_df['Rating text'],
                'values': restaurant_counts_df['Count'],
                'hoverinfo': 'label+percent',
                'hole': .7,
                'type': 'pie',
                'marker': {
                    'colors': ['#0052cc', '#3385ff', '#99c2ff']
                },

                'showlegend': True
            }],

            'layout': {
                'title' : dict(text="Rating Distribution",
                                font=dict(size=20,
                                          color='white')
                ),

                'paper_bgcolor':'#111111',
                'showlegend':True,
                'height':600,
                'marker': {
                    'colors': ['#0052cc', '#3385ff', '#99c2ff']
                },

                'annotations': [{
                        'font': {'size': 20},
                        'showarrow': False,
                        'text': '',
                        'x': 0.2,
                        'y': 0.2
                }],

                'showlegend': True,
                'legend': dict(
                    fontColor='white',
                    tickfont={'color':'white'}
                ),
                
                'legenditem': {
                    'textfont': {'color':'white'}
                }
            }
        }
)
