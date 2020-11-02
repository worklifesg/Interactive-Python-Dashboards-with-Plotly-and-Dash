# Take advantage of Dash State, and hold all API calls until a Submit button is pressed to update plot

import dash 
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input,Output,State

import pandas_datareader.data as web
from datetime import datetime

app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.H2('Asia Indices'),
    html.Div([
        html.H3('Enter a stock symbol:', style={'paddingRight':'30px'}),
        dcc.Input(
            id='my_ticker_symbol',
            value='TSLA', # sets a default value
            style={'fontSize':24, 'width':75}
        )
    ], style={'display':'inline-block', 'verticalAlign':'top'}),
    html.Div([
        html.H3('Select start and end dates:'),
        dcc.DatePickerRange(
            id='my_date_picker',
            min_date_allowed = datetime(2015, 1, 1),
            max_date_allowed = datetime.today(),
            start_date = datetime(2018, 1, 1),
            end_date = datetime.today()
        )
    ], style={'display':'inline-block'},
    ),
    html.Div([
            html.Button(id='submit-button',
            n_clicks=0,
            children='Submit',
            style={'fontsize':24,'marginLeft':'30px'})
    ],style={'display':'inline-block'}),
    dcc.Graph(
        id='my_graph',
        figure={
            'data': [
                {'x': [1,2], 'y': [3,1]}
            ]
        }
    )
],style={'width':'60%','display':'inline-block'})
@app.callback(
    Output('my_graph', 'figure'),
    [Input('submit-button','n_clicks')],
    [State('my_ticker_symbol', 'value'), #change input tp state
    State('my_date_picker', 'start_date'),
    State('my_date_picker', 'end_date')])
def update_graph(n_clicks,stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    df = web.DataReader(stock_ticker,'stooq',start,end)
    fig = {
        'data': [
            {'x': df.index, 'y': df.Close}
        ],
        'layout': {'title':stock_ticker}
    }
    return fig

if __name__ == '__main__':
    app.run_server()
