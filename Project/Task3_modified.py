# Ensure that we can read data off the web using pandas datareader

# pandas_datareader to connect to internet and collect live updated data from the web !pip install pandas_datareader

import dash 
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input,Output

import pandas_datareader.data as web
from datetime import datetime

app = dash.Dash()

app.layout = html.Div([
            html.Div([
                html.H1('Stock Ticker DashBoard'),
                html.H2('Asia Indices'),
                html.H3('Enter a stock symbol: '),
                dcc.Input(id='my_stock_picker',
                          value='^SNX'),
                dcc.Graph(id='my_graph',
                          figure={'data':[{'x':[1,2],'y':[3,1]},
                          ],'layout':{'title':'Default Title'}} # We add default title in Task 1 Code
                )
],style={'width':'48%','display':'inline-block'}),
            html.Div([html.H2('America Indices'),
                html.H3('Enter a stock symbol: '),
                dcc.Input(id='my_stock_picker2',
                          value='^SPX'),
                dcc.Graph(id='my_graph2',
                          figure={'data':[{'x':[1,2],'y':[3,1]}
                          ],'layout':{'title':'Default Title'}} # We add default title in Task 1 Code
                ),

],style={'width':'48%','display':'inline-block'}),
            html.Div([html.H2('Europe Indices'),
                html.H3('Enter a stock symbol: '),
                dcc.Input(id='my_stock_picker3',
                          value='^PX'),
                dcc.Graph(id='my_graph3',
                          figure={'data':[{'x':[1,2],'y':[3,1]}
                          ],'layout':{'title':'Default Title'}} # We add default title in Task 1 Code
                ),

],style={'width':'48%','display':'inline-block'}),
            html.Div([html.H2('Middle East Indices'),
                html.H3('Enter a stock symbol: '),
                dcc.Input(id='my_stock_picker4',
                          value='^TASI'),
                dcc.Graph(id='my_graph4',
                          figure={'data':[{'x':[1,2],'y':[3,1]}
                          ],'layout':{'title':'Default Title'}} # We add default title in Task 1 Code
                ),

],style={'width':'48%','display':'inline-block'})
])

@app.callback(Output('my_graph','figure'),
              [Input('my_stock_picker','value')])
def update_graph(stock_ticker):
    start = datetime(2020,1,1) 
    end = datetime(2020,10,31) 
    df = web.DataReader(stock_ticker,'stooq',start,end)
    fig = {'data':[{'x':df.index,'y':df.Close}],
            'layout':{'title':stock_ticker}}
    return fig


@app.callback(Output('my_graph2','figure'),
              [Input('my_stock_picker2','value')])
def update_graph(stock_ticker2):
    start = datetime(2020,1,1) 
    end = datetime(2020,10,31) 
    df = web.DataReader(stock_ticker2,'stooq',start,end)
    fig = {'data':[{'x':df.index,'y':df.Close}],
            'layout':{'title':stock_ticker2}}
    return fig

@app.callback(Output('my_graph3','figure'),
              [Input('my_stock_picker3','value')])
def update_graph(stock_ticker3):
    start = datetime(2020,1,1) 
    end = datetime(2020,10,31) 
    df = web.DataReader(stock_ticker3,'stooq',start,end)
    fig = {'data':[{'x':df.index,'y':df.Close}],
            'layout':{'title':stock_ticker3}}
    return fig

@app.callback(Output('my_graph4','figure'),
              [Input('my_stock_picker4','value')])
def update_graph(stock_ticker4):
    start = datetime(2020,1,1) 
    end = datetime(2020,10,31) 
    df = web.DataReader(stock_ticker4,'stooq',start,end)
    fig = {'data':[{'x':df.index,'y':df.Close}],
            'layout':{'title':stock_ticker4}}
    return fig

if __name__ == "__main__":
    app.run_server()
