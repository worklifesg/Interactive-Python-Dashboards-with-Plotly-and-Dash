# In this program we will make dash components (HTML and core) interactive using @callbacks

# In this program we will get multiple outputs using callbacks with help of decorator pairs to the scripts

# Version 2: Display image corresponding to the selection (Will need images folder from where inages are picked up and displayed)

import dash
import dash_core_components as  dcc 
import dash_html_components as html 
import pandas as pd 
from dash.dependencies import Input,Output
import plotly.graph_objs as go

import base64 # to import images

#Read dataset 'wheels.csv'

df = pd.read_csv('wheels.csv')

app = dash.Dash()

# Reading images and function to display them
def encode_image(image_file):
    encoded = base64.b64encode(open(image_file,'rb').read()) #read an image_files and open it and read binary
    return 'data:image/png;base64,{}'.format(encoded.decode()) #display the iamge as png file


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
            html.Div(id='colors-output'), #output for colors
            html.Img(id='display-image',src='children',height=300)
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


@app.callback(Output('display-image','src'),
              [Input('wheels','value'),
              Input('colors','value')])

# Function to callback image

def callback_image(wheel,color):
    return encode_image(df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0])


if __name__ == "__main__":
    app.run_server()
