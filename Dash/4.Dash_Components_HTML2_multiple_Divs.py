# Here we will try to have multiple Divs and style them

#import libraries

import dash 
import dash_html_components as html 

app = dash.Dash()

app.layout = html.Div(['This is the outermost div!',
                        html.Div(['This is an inner div!'], #better to ahve every div in list, to be on sure side
                        style={'color':'red'})], #multiple components must be in a list else it can be string
                       style={'color':'green','border':'2px green solid'})# any CSS calls 


if __name__ =='__main__':
    app.run_server()
