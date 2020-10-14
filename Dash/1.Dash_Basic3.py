# In this code, we will add core components (dcc) with html components


import dash
import dash_core_components as dcc
import dash_html_components as html 

#create application

app = dash.Dash() #creating app like a Flask application

#Layouts
#Create a division in dashboard to innert links
#with variable children that has a list
app.layout = html.Div(children=[
            html.H1('Hello Dash!'), #html components
            html.Div('Dash: Web Dashboards with Python'),
            dcc.Graph(id='example',  #reference id - adding graph from core components
                      figure={'data':[ #two key components inside figure: data and layout
                               {'x':[1,2,3],'y':[4,1,2],'type':'bar','name':'SF'}, #manually creating charts/ later will do plotly data
                               {'x':[1,2,3],'y':[2,4,5],'type':'bar','name':'NYC'},
                               ],
                                    'layout':{
                                    'title':'BAR PLOTS !'
                                    }})
]) 

if __name__ == '__main__':
    app.run_server() # just checks if we running our script or not, grab the application ('app') and run the server

