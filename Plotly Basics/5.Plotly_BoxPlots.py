# In this script, we will analyze box plots using plotly functions

import plotly.offline as pyo 
import plotly.graph_objs as go 

#----------------------- Constructing a simple box plot------------------------

# set up an array of 20 data points, with 20 as the median value
y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

data =[go.Box(y=y,  #No categorical x column
        boxpoints='all', #boxpoints, displays all original data points
        jitter=0.3, #spread all values properly 
        pointpos=2)]  #offset points to left (-ve) or right (+ve)
layout = go.Layout(
    title = 'Simple Box Plot'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig,filename='Simple-Box-Plot.html')

#---------------------- Displaying only outliers -------------------------------

data1 =[go.Box(y=y,  #No categorical x column
        boxpoints='outliers', #boxpoints, displays outliers data points
        jitter=0.3, #spread all values properly 
        pointpos=2)]  #offset points to left (-ve) or right (+ve)
layout1 = go.Layout(
    title = 'Outliers Box Plot'
)
fig1 = go.Figure(data=data1, layout=layout1)
pyo.plot(fig1,filename='Outliers-Box-Plot.html')

#---------------------- Mark Twain Data -------------------------------
'''
 As a forensic example of applied statistics, there was a famous case where Mark twain was accused of being a Confederate deserter during 
 Civil War. The evidence given were 10 essays published in New Orleans Daily Crescent under the name Quintus Curtius Snodgrass.

 In 1963, Claude Brinegar published an article in the Journal of the American Statistical Association where he uses word frequencies and a chi-squared
 test to show that the essays were almost certainly not Twain's because of different usage of length of words

 In this example we will compare the word length counts between two authors
'''

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

data2 =[go.Box(y=snodgrass,
        name='Snodgrass',  #No categorical x column
        boxpoints='all', #boxpoints, displays outliers data points
        jitter=0.3, #spread all values properly 
        pointpos=2),#offset points to left (-ve) or right (+ve)

        go.Box(y=twain,
        name='Twain',  #No categorical x column
        boxpoints='all', #boxpoints, displays outliers data points
        jitter=0.3, #spread all values properly 
        pointpos=2)]  

layout2 = go.Layout(
    title = 'Snodgrass-Twain Box Plot'
)
fig2 = go.Figure(data=data2, layout=layout2)
pyo.plot(fig2,filename='Snodgrass-Twain-Box-Plot.html')

'''
Based on usage of words by both authors, it is sure twain is not snodgrass
'''

#-----------------------------------------------------------------------------------------------------------#
