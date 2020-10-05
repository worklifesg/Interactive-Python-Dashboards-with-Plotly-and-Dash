# In this script, we will analyze line charts using plotly functions (this code is for all types of line charts)

import numpy as np
import plotly.offline as pyo 
import plotly.graph_objs as go 

#intialzing some random numbers
np.random.seed(56) #to generate same data everytime

x_values = np.linspace(0,1,100) #100 evenly (ordered) spaced values
y_values = np.random.randn(100) #100 random values for thse x_values

# Line chart we create a trace

trace0 = go.Scatter(x=x_values,y=y_values+5, #add 5 to every y generated random value
                    mode='markers',name='markers')

trace1 = go.Scatter(x=x_values,y=y_values,
                    mode='lines',name='mylines')

trace2 = go.Scatter(x=x_values,y=y_values-5,
                    mode='lines+markers',name='mylines+markers')

data = [trace0, trace1,trace2] #put trace0 and 1 in a data list

layout = go.Layout(title='Line Charts')

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Line-Chart-with-lines-markers.html')
