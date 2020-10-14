# In this code, we will add styles to graph and layout


import dash
import dash_core_components as dcc
import dash_html_components as html 

#create application

app = dash.Dash() #creating app like a Flask application

colors = {'background':'#111111','text':'#7FDBFF'} #colors dictionary - better to call dictionary rather than making code more complex


#Layouts
#Create a division in dashboard to innert links
#with variable children that has a list
app.layout = html.Div(children=[
            html.H1('Hello Dash!',style={'textAlign':'center', #style with different CSS templates and styles
                                         'color':colors['text']}),
            dcc.Graph(id='example',  #reference id - adding graph from core components
                    figure={'data':[ #two key components inside figure: data and layout
                    {'x':[1,2,3],'y':[4,1,2],'type':'bar','name':'SF'}, #manually creating charts/ later will do plotly data
                    {'x':[1,2,3],'y':[2,4,5],'type':'bar','name':'NYC'}
                    ],
                            'layout':{
                            'plot_bgcolor':colors['background'], #background color of plot
                            'paper_bgcolor':colors['background'], #colors outside grid area
                            'font':{'color':colors['text']}, #font color 
                            'title':'BAR PLOTS !'
                             }})
], style={'backgroundColor':colors['background']} #styling whole layout
) 

if __name__ == '__main__':
    app.run_server() # just checks if we running our script or not, grab the application ('app') and run the server

