# Here we will try to have multiple Divs and style them

#import libraries

import dash 
import dash_html_components as html 

app = dash.Dash()

app.layout = html.Div(['This is the outermost div!',
                        html.Div(['This is an inner div!'], #better to ahve every div in list, to be on sure side
                        style={'color':'red','border':'2px red solid'}),
                        html.Div(['Another inner div'],
                        style={'color':'blue','border':'3px blue solid'})], #multple components must be in alist else it can be string
                       style={'color':'green','border':'2px green solid'})# any CSS calls 

if __name__ =='__main__':
    app.run_server()
