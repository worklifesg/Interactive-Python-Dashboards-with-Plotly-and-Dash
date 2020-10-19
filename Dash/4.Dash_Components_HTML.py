# In the code, we will see HTML components such as Div and CSS styles in details

#import libraries

import dash 
import dash_html_components as html 

app = dash.Dash()

app.layout = html.Div(['This is the outermost div!'], #passing single string into list
                       style={'color':'green','border':'2px green solid'})# any CSS calls 


if __name__ =='__main__':
    app.run_server()
