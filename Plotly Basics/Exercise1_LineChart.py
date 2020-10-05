#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:

import pandas as pd 
import numpy as np
import plotly.offline as pyo 
import plotly.graph_objs as go

# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']

print(df.head())

# Use a for loop (or list comprehension to create traces for the data list)
data = []

for day in days:
    trace = go.Scatter(x=df['LST_TIME'],
                        y=df[df['DAY']==day]['T_HR_AVG'],
                        mode='lines',
                        name=day)
    data.append(trace)

layout = go.Layout(title='Daily temperature from June1-7, 2010 in Yuma, Arizona',
                    xaxis={'title':'Time'}, #can use {} approach
                    yaxis=dict(title='Temperature'), #can use dict also
                    hovermode='closest') #handle multiple points on the same data (both x and y)

fig =go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Daily-Temperature-Yuma-2010.html')

