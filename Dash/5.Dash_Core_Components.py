# In this program we will understand core components of DASH - higher level calls

# https://dash.plotly.com/dash-core-components

# Simple components will be discussed here

import dash 
import dash_html_components as html 
import dash_core_components as dcc 

app = dash.Dash()

app.layout = html.Div([

            html.Label('Dropdown'),
            dcc.Dropdown(options=[{'label':'New York City', #Dropdown has options
                                    'value':'NYC'},
                                    {'label':'San Francisco',
                                    'value':'SF'}],
                        value='SF'), #default value SF
            
            html.Label('Slider'), #Slider has min and max values
            dcc.Slider(min=-10,max=10,step=0.5,value=0, #can give marks also but gave value as 0
                        marks={i: i for i in range(-10,10)}) 

])

if __name__ =='__main__':
    app.run_server()
