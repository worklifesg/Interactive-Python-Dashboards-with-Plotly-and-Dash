# In this script, we will analyze scatter plots using plotly functions

import numpy as np
import plotly.offline as pyo 
import plotly.graph_objs as go 

#intialzing some random numbers
np.random.seed(42) #to generate same data everytime

random_x=np.random.randint(1,101,100) #100 random integers from 1 to 101
random_y=np.random.randint(1,101,100)

#some nesting of list in a nest
data = [go.Scatter(x=random_x,y=random_y,mode='markers')] #empty list - with x and y arguments and mode=markers points for scatter plot

#will put some labels, layout and hovering

layout = go.Layout(title='Hello First Plot: Scatter Plot',
                    xaxis={'title':'MY X AXIS'}, #can use {} approach
                    yaxis=dict(title='MY Y AXIS'), #can use dict also
                    hovermode='closest') #handle multiple points on the same data (both x and y)

fig =go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='scatter-plot.html')

#-----------------------------------------------------------------------------------------------------------------#

#some nesting of list in a nest
data1 = [go.Scatter(x=random_x,
                    y=random_y,
                    mode='markers',
                    marker=dict(
                        size=12, #size of marker
                        color='rgb(51,204,153)', #color of color , can be hexa color as well
                        symbol='pentagon', #the shape of symbol is a string here
                        line={'width':2} #width of line outside the point
                    ))] #empty list - with x and y arguments and mode=markers points for scatter plot

#will put some labels, layout and hovering

layout1 = go.Layout(title='Scatter Modified Plot',
                    xaxis={'title':'MY X AXIS'}, #can use {} approach
                    yaxis=dict(title='MY Y AXIS'), #can use dict also
                    hovermode='closest') #handle multiple points on the same data (both x and y)

fig1 =go.Figure(data=data1,layout=layout1)
pyo.plot(fig1,filename='scatter-plot-modified.html')

