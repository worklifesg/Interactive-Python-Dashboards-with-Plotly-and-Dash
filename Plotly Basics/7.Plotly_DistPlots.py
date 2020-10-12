# In this script, we will analyze Distribution plots (DistPlot) using plotly functions

import plotly.offline as pyo 
import plotly.figure_factory as ff # for complex visualizations
import numpy as np

x = np.random.randn(1000) #generating random 1000 data points

# Basic Distplot
hist_data = [x] #list of data points
group_labels=['Distplot'] #labels

fig=ff.create_distplot(hist_data,group_labels=group_labels) # using ff.create
pyo.plot(fig,filename='Basic-Distplot.html')

#----------------------------------------------------------------------------------#

#Multiple groups (4)

x1 = np.random.randn(200)-2
x2 = np.random.randn(200) 
x3 = np.random.randn(200)+2 
x4 = np.random.randn(200)+4 #shifting so they don't overlap

hist_data1 = [x1,x2,x3,x4] #list of data points
group_labels1=['X1','X2','X3','X4'] #labels

fig1=ff.create_distplot(hist_data1,group_labels=group_labels1) # using ff.create
pyo.plot(fig1,filename='Multigroup-Distplot.html')

#----------------------------------------------------------------------------------#

#Multiple groups (4) with different bin size

fig2=ff.create_distplot(hist_data1,group_labels=group_labels1, bin_size=[0.2,0.1,0.3,0.4]) # using ff.create
pyo.plot(fig2,filename='Multigroup-Distplot-BinSize.html')

#----------------------------------------------------------------------------------#

#Snodgrass  - Twain problem (better than box plots)

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]


hist_data3 = [snodgrass,twain] #list of data points
group_labels3=['Snodgrass Writings','Mark Twain Writings'] #labels

fig3=ff.create_distplot(hist_data3,group_labels=group_labels3,bin_size=[0.005,0.005]) # using ff.create
pyo.plot(fig3,filename='SnodgrassTwain-Distplot.html')
