# Add an input box and a basic callback to display the input value (the ticker) on the graph. 

import dash 
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input,Output

app = dash.Dash()

app.layout = html.Div([
                html.H1('Stock Ticker DashBoard'),
                html.H3('Enter a stock symbol: '),
                dcc.Input(id='my_stock_picker',
                          value='TSLA'),
                dcc.Graph(id='my_graph',
                          figure={'data':[{'x':[1,2],'y':[3,1]}
                          ],'layout':{'title':'Default Title'}} # We add default title in Task 1 Code
                )
])

@app.callback(Output('my_graph','figure'),
              [Input('my_stock_picker','value')])

# function for callback
def update_graph(stock_ticker):
     fig = {'data':[{'x':[1,2],'y':[3,1]}],
            'layout':{'title':stock_ticker}
     }
     return fig

if __name__ == "__main__":
    app.run_server()
    
