# In this program we will make dash components (HTML and core) interactive using @callbacks

# In this program we will use multiple inputs to a single output using callback only

import dash
import dash_core_components as  dcc 
import dash_html_components as html 
import pandas as pd 
from dash.dependencies import Input,Output
import plotly.graph_objs as go 

df = pd.read_csv('mpg.csv')

app = dash.Dash()

# List of features we will be working on, in the dropdown
features = df.columns #['mpg','hp','displacement'....]

# Bascially three things - 2 dropdowns for x and y axis and a graph
app.layout = html.Div([
            html.Div([
                dcc.Dropdown(id='xaxis', #Features
                             options=[{'label':i, 'value':i} for i in features],
                             value='displacement')
            ],style={'width':'48%','display':'inline-block'}), #inline-block is to place next dropdown next to the first one
            html.Div([
                dcc.Dropdown(id='yaxis', #Features
                             options=[{'label':i, 'value':i} for i in features],
                             value='mpg')
            ],style={'width':'48%','display':'inline-block'}),
            dcc.Graph(id='feature-graphic')


],style={'padding':10}) # styling for entire dashboard

# callbacks
@app.callback(Output('feature-graphic','figure'),
            [Input('xaxis','value'),
            Input('yaxis','value')])

def update_graph(xaxis_name,yaxis_name):
    return {'data':[go.Scatter(x=df[xaxis_name],
                                y=df[yaxis_name],
                                text=df['name'],
                                mode='markers',
                                marker={'size':15})]
    ,'layout': go.Layout(title='My Dashboard for MPG',
                xaxis={'title':xaxis_name},
                yaxis={'title':yaxis_name})}


if __name__ == "__main__":
    app.run_server()

