#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:

import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objs as go 


# create a DataFrame from the .csv file:

df=pd.read_csv('mpg.csv')
print(df.head())
# create data by choosing fields for x, y and marker size attributes
# We will choose, acceleration vs displacement along with weight and no. of cylinders in scale bar

data = [go.Scatter(x=df['displacement'],
                   y=df['acceleration'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=0.01*df['weight'],
                   color=df['cylinders'],
                   showscale=True))]

layout = go.Layout(title='Bubble Chart (Acc vs Dis)',
                    xaxis=dict(title='Displacment'),
                    yaxis=dict(title='Acceleration'),
                    hovermode='x')

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Bubble-Chart-Exercise.html')
