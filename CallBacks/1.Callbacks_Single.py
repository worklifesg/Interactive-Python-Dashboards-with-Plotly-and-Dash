# In this program we will start making dash components (HTML and core) interactive using @callbacks

# In this first program we will use single (one component) callback only

import dash  
import dash_core_components as dcc  
import dash_html_components as html 

from dash.dependencies import Input,Output

app = dash.Dash()

# Single core component taking text as input and nothing is displayed as it is just to write a text in a box

app.layout = html.Div([
            dcc.Input(id='my-id',
                      value='Intial Text',
                      type='text'),
                      html.Div(id='my-div') #style={'border':'2px blue solid'} for styling div
])

# Now if we use callbacks we can make our above core component interactive 

#for decoration
@app.callback(Output(component_id='my-div', #Output - html.div
                     component_property='children'), #children - first text you write
                     [Input(component_id='my-id', #Input - dcc.Input
                     component_property='value')]) 

def update_output_div(input_value):
    return 'You entered: {}'.format(input_value) #function to generate output

if __name__ == "__main__":
    app.run_server()
