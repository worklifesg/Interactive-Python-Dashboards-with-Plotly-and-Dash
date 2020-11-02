#  Perform imports, set up a graph with static data, ensure that we can lay everything out on the screen

import dash 
import dash_core_components as dcc
import dash_html_components as html 

app = dash.Dash()

app.layout = html.Div([
                html.H1('Stock Ticker DashBoard'),
                html.H3('Enter a stock symbol: '),
                dcc.Input(id='my_stock_picker',
                          value='TSLA'),
                dcc.Graph(id='my_graph',
                          figure={'data':[{'x':[1,2],'y':[3,1]}
                          ]}
                )
])

if __name__ == "__main__":
    app.run_server()
    
