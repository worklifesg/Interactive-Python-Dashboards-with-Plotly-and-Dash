# In this program we will make dash components (HTML and core) interactive using @callbacks

# In this program we will get multiple outputs using callbacks with help of decorator pairs to the scripts

# Version 1: Display outputs back as text

import dash
import dash_core_components as  dcc 
import dash_html_components as html 
import pandas as pd 
from dash.dependencies import Input,Output
import plotly.graph_objs as go

#Read dataset 'wheels.csv'

df = pd.read_csv('wheels.csv')

app = dash.Dash()

app.layout = html.Div([
            dcc.RadioItems(id='wheels',
                            options=[{'label':i,'value':i} for i in df['wheels'].unique()], # To choose from wheels 1,2,3 (i) from df wheels column
                            value=1
                            ),
            html.Div(id='wheels-output'), #output of the chosen number of wheels
            html.Hr(), #add horizontal rule in between two Radio items
            dcc.RadioItems(id='colors',
                           options=[{'label':i,'value':i} for i in df['color'].unique()], # to choose from color, default color is blue
                           value='blue'
                           ),  # for color
            html.Div(id='colors-output') #output for colors
],style={'fontFamily':'helvetca','fontSize':18})

# callbacks

@app.callback(Output('wheels-output','children'), #for wheels
             [Input('wheels','value')])
def callback_a(wheels_value):
    return 'You chose {}'.format(wheels_value)

@app.callback(Output('colors-output','children'), #for colors
             [Input('colors','value')])
def callback_b(colors_value):
    return 'You chose {}'.format(colors_value)

if __name__ == "__main__":
    app.run_server()
