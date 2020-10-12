#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:

import plotly.offline as pyo 
import plotly.figure_factory as ff
import pandas as pd 

# create a DataFrame from the .csv file:

df = pd.read_csv('iris.csv')

# Define the traces

trace_0 = df[df['class']=='Iris-setosa']['petal_length']
trace_1= df[df['class']=='Iris-versicolor']['petal_length']
trace_2 = df[df['class']=='Iris-virginica']['petal_length']

# Define a data variable

hist_data = [trace_0,trace_1,trace_2]
group_labels = ['Iris-setosa','Iris-versicolor','Iris-virginica']

# Create a fig from data and layout, and plot the fig

fig = ff.create_distplot(hist_data,
                        group_labels=group_labels,
                        bin_size=[0.1,0.2,0.2])
pyo.plot(fig,filename='Iris-DistPlot.html')
