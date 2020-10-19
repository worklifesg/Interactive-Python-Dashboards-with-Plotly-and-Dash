#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######
'''
Old Faithful - cone geyser located in Yellowstone National Park in Wyoming US
Since 2000, its intervals varied from 44 to 125 minutes between eruptions

It is currentlky binodal. It has two eruption duration either long (over 4 minutes) or rarely
short about 2.5 minutes

Short eruptions lead to interval of just over an hour
Long eruptions lead to interval of about 1.5 hours

'''
# Perform imports here:

import dash
import dash_core_components as dcc 
import dash_html_components as html 

import plotly.graph_objs as go 
import pandas as pd  

# Launch the application:

app = dash.Dash()

# Create a DataFrame from the .csv file:

df = pd.read_csv('OldFaithful.csv')

# Create a Dash layout that contains a Graph component:

app.layout = html.Div([dcc.Graph(id='exercise',
                             figure = {'data':[
                                        go.Scatter(x=df['X'],y=df['Y'],
                                        mode='markers',
                                        marker={
                                                'size':8,
                                                'color':'rgb(51,204,153)',
                                                'symbol':'pentagon',
                                                'line':{'width':2}
                                        })],
                                        'layout': go.Layout(title='Old Faithful Eruption Intervals vs Durations',
                                                            xaxis={'title':'Duration of eruption (minutes)'},
                                                            yaxis={'title':'Interval to next eruption (minutes)'}
                                                            )}   
                                        )])

if __name__=='__main__':
    app.run_server()
