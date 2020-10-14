# In this program we will insert plotly graphs inside a dash

#import dash and plotly libraries
import dash 
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go 
import numpy as np 

#create app
app = dash.Dash()

#Creating data
np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

#dash
app.layout = html.Div([dcc.Graph(id='scatterplot',
                                figure = {'data':[
                                          go.Scatter(x=random_x,y=random_y,
                                          mode='markers')],
                                          'layout':go.Layout(title='Scatter Plot')}
                                )])

if __name__ == '__main__':
    app.run_server() 
