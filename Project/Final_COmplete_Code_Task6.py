#  Replace the input box with a multiple dropdown list of choices. Pass multiple stocks as traces on the same graph.

import dash 
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input,Output,State

import pandas_datareader.data as web
from datetime import datetime
import pandas as pd 

app = dash.Dash()

# Create a list of options NASDAQ

nsdq = pd.read_csv('NASDAQcompanylist.csv')
nsdq.set_index('Symbol',inplace=True)
# nsdq = nsdq.set_index('Symbol')

options=[]
for tic in nsdq.index:
    #{'label':'usersees', 'value':'script sees'}
    mydict={}
    mydict['label'] = str(nsdq.loc[tic]['Name'])+' '+tic # Apple Co.APPL
    mydict['value'] = tic
    options.append(mydict)

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.Div([
        html.H3('Enter a stock symbol:', style={'paddingRight':'30px'}),
        dcc.Dropdown(
            id='my_ticker_symbol',
            options=options,
            value=['TSLA'], # sets a default value
            multi=True #for chosing multiple options
        )
    ], style={'display':'inline-block', 'verticalAlign':'top','width':'30%'}),
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
],style={'width':'100%','display':'inline-block'})
@app.callback(
    Output('my_graph', 'figure'),
    [Input('submit-button','n_clicks')],
    [State('my_ticker_symbol', 'value'), #change input tp state
    State('my_date_picker', 'start_date'),
    State('my_date_picker', 'end_date')])
def update_graph(n_clicks,stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')

    traces = []
    for tic in stock_ticker:
        df = web.DataReader(tic,'stooq',start,end) #multi stock ticker
        traces.append({'x': df.index, 'y': df.Close,'name':tic})
    fig = {
        'data': traces,
        'layout': {'title':stock_ticker}
    }
    return fig

if __name__ == '__main__':
    app.run_server()
