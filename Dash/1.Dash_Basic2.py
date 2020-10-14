import dash
import dash_core_components as dcc
import dash_html_components as html 

#create application

app = dash.Dash() #creating like a Flask application

#Layouts
#Create a division in dashboard to innert links
#with variable children that has a list
app.layout = html.Div(children=[
            html.H1('Hello Dash!'), #header
            html.Div('Dash: Web Dashboards with Python')
]) 

if __name__ == '__main__':
    app.run_server() # just checks if we running our script or not, grab the application ('app') and run the server

