# In this script, we will analyze histogram plots using plotly functions

import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

#Read Dataset ('/mpg.csv')
df = pd.read_csv('mpg.csv')

# Histogram plot

data = go.Histogram(x=df['mpg']) #continous feature analysis
layout = go.Layout(title='Histogram')

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Simple-Histogram-Plot.html')

#-----------------------------------------------------------------------#
# Wide bin values but not much details #

data1 = go.Histogram(x=df['mpg'],
                    xbins=dict(start=0,end=50,size=10)) #display histogram from 0 to 50 mpg with each bin of 10 mpg
layout1 = go.Layout(title='Histogram for MPG (0-50 mpg) with each bin = 10 mpg')

fig1 = go.Figure(data=data1,layout=layout1)
pyo.plot(fig1,filename='Modified-Histogram-Plot.html')

#-----------------------------------------------------------------------#
# Narrower bin values with details #

data2 = go.Histogram(x=df['mpg'],
                    xbins=dict(start=0,end=50,size=1)) #display histogram from 0 to 50 mpg with each bin of 1 mpg
layout2 = go.Layout(title='Histogram for MPG (0-50 mpg) with each bin = 1 mpg')

fig2 = go.Figure(data=data2,layout=layout2)
pyo.plot(fig2,filename='Modified2-Histogram-Plot.html')

#-----------------------------------------------------------------------#
