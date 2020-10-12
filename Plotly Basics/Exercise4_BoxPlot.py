#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:

import plotly.offline as pyo 
import plotly.graph_objs as go
import pandas as pd 
import numpy as np 

# create a DataFrame from the .csv file:

df = pd.read_csv('abalone.csv')

# take two random samples of different sizes:

p = np.random.choice(df['rings'],30,replace=False)
q = np.random.choice(df['rings'],300,replace=False)

# create a data variable with two Box plots:

data = [go.Box(y=p,
        name='P',
        boxpoints='all',
        pointpos=2),

        go.Box(y=q,
        name='Q',
        boxpoints='all',
        pointpos=2)]
        
# add a layout

layout = go.Layout(title='Comparison of two samples P and Q')

# create a fig from data & layout, and plot the fig

fig=go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Box-Plot-Exercise.html')

