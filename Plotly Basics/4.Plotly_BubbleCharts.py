# In this script, we will analyze bubble charts using plotly functions

import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objs as go 

#Data read
df=pd.read_csv('mpg.csv')

#print(df)
#print(df.columns) # 'mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'

data = [go.Scatter(x=df['horsepower'], #setup out data list
                    y=df['mpg'],
                    text = df['name'], #text for hovering
                    mode = 'markers', 
                    marker=dict(size=2*df['cylinders']))] #making bubble chart by giving another feature in chart and multiplying 2 with no. of cylinders to have some significance
                    # example for weight we can make it smaller as to determine pixels of bubbles smaller

layout = go.Layout(title='Bubble Chart (HP vs MPG) wrt cylinders',
                    xaxis={'title':'MPG'},
                    yaxis=dict(title='Horsepower')
                    )
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Bubble-Chart-cylinders.html')

#---------------------------------------------------------#

# now checking with weight of car

data1 = [go.Scatter(x=df['horsepower'], #setup out data list
                    y=df['mpg'],
                    text = df['name'], #text for hovering
                    mode = 'markers', 
                    marker=dict(size=0.01*df['weight']))] # 0.01 to avoid huge marker size

layout1 = go.Layout(title='Bubble Chart (HP vs MPG) wrt weight',
                    xaxis={'title':'MPG'},
                    yaxis=dict(title='Horsepower')
                    )
fig1= go.Figure(data=data1,layout=layout1)
pyo.plot(fig1,filename='Bubble-Chart-weight.html')

#---------------------------------------------------------#

# Now let's add some categorical values for bubble chart (coloring)

data2 = [go.Scatter(x=df['horsepower'], #setup out data list
                    y=df['mpg'],
                    text = df['name'], #text for hovering
                    mode = 'markers', 
                    marker=dict(size=0.01*df['weight'],color=df['cylinders'], #adding cylinders as categorical features 
                    showscale=True))] # showscale to no. of cylinders on its scale

layout2 = go.Layout(title='Bubble Chart (HP vs MPG) wrt weight',
                    xaxis={'title':'MPG'},
                    yaxis=dict(title='Horsepower'),
                    hovermode='x') #hovering over x or y or closest
fig2= go.Figure(data=data2,layout=layout2)
pyo.plot(fig2,filename='Bubble-Chart-categorical.html')

#----------------------------------------------------------------------------------------#
