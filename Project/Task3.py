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
                html.H1('Stock Ticker DashBoard'),
                html.H3('Enter a stock symbol: '),
                dcc.Input(id='my_stock_picker',
                          value='^SPX'),
                dcc.Graph(id='my_graph',
                          figure={'data':[{'x':[1,2],'y':[3,1]}
                          ],'layout':{'title':'Default Title'}} # We add default title in Task 1 Code
                )
])

@app.callback(Output('my_graph','figure'),
              [Input('my_stock_picker','value')])

# function for callback (Updated in Task 3)
def update_graph(stock_ticker):

    start = datetime(2020,1,1) #1 Jan 2017 start date
    end = datetime(2020,10,31) #31 Dec 2017 end date
    df = web.DataReader(stock_ticker,'stooq',start,end)
    fig = {'data':[{'x':df.index,'y':df.Close}],
            'layout':{'title':stock_ticker}}
    return fig

if __name__ == "__main__":
    app.run_server()
