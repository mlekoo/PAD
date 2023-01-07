# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 22:05:25 2023

@author: Mleko
"""


import plotly.express as px
import pandas as pd
from dash import Dash, dash_table, html, dcc, Input, Output

app = Dash(__name__)

df = pd.read_csv('winequelity.csv', index_col=0)

app.layout = html.Div(style={'backgroundcolor': '#88878'}, children=[
    html.Div(
        children=dash_table.DataTable(
            df.head(10).to_dict('records'), 
            [{"name": i, "id": i} for i in df.columns]
        )
    ),
    html.P(),
    html.Div(style={'align':'left', 'width' : '10%'},children=[
        dcc.Slider(0,1,step=None,marks={0:'Regression',1: 'Classification'},value=0, id='slider')
    ]),
    
    html.Div([
        dcc.Slider(0, df.columns.size,step=None,marks={i: '{}'.format(df.columns[i]) for i in range(0,df.columns.size)},value=0, id='slider-choice')
    ]),

    html.P(),

    html.Div([
        dcc.Graph(id='graph-for-user')
    ])
])

def update_plot_layout(fig):
    fig.update_layout(
        plot_bgcolor='black',
        paper_bgcolor='black',
        font_color='white'
    )

# Define page actions
@app.callback(
    Output('graph-for-user', 'figure'),
    Input('slider', 'value'),
    Input('slider-choice', 'value')
)

def update_figure(value_slider, value_menu):
    if value_slider == 0:#regression
        fig = px.bar(df, x='pH', y=df.columns[value_menu])
        update_plot_layout(fig)

    elif value_slider == 1: #classification
        fig = px.scatter(df, x=df.columns[value_menu], y='target')
        update_plot_layout(fig)

    else:
        return f'Value {value_slider} is not supported'
    
    return fig

# Run application
if __name__ == '__main__':
    app.run_server(debug=True)