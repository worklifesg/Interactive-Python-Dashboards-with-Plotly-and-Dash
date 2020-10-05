# In this script, we will analyze bar charts using plotly functions

import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objs as go 

#Data read
df=pd.read_csv('2018WinterOlympics.csv')

#Bar Chart (General)

data =[go.Bar(x=df['NOC'],
        y=df['Total'])]

layout = go.Layout(title='Total Medals in WInter Olympics 2018',
                    xaxis={'title':'Countries'}, #can use {} approach
                    yaxis=dict(title='Total medals'), #can use dict also
                    hovermode='closest') #handle multiple points on the same data (both x and y)

fig =go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Bar-Chart-Simple.html')

#Bar Chart for each type (Nested Bar Chart)

trace1=go.Bar(x=df['NOC'],
        y=df['Gold'],
        name='Gold',
        marker={'color':'#FFD700'}) # for gold color
trace2=go.Bar(x=df['NOC'],
        y=df['Silver'],
        name='Silver',
        marker={'color':'#9EA0A1'}) #for silver color
trace3=go.Bar(x=df['NOC'],
        y=df['Bronze'],
        name='Bronze',
        marker={'color':'#CD7F32'}) #for bronze color


data1=[trace1,trace2,trace3]
layout1 = go.Layout(title='Total Medals in Winter Olympics 2018 (Nested Bar Chart)',
                    xaxis={'title':'Countries'}, #can use {} approach
                    yaxis=dict(title='Medals')) #can use dict also

fig1 =go.Figure(data=data1,layout=layout1)
pyo.plot(fig1,filename='Bar-Chart-Nested.html')

#Stacked Bar Chart - just change layout to 'stack' in nested bar chart code

layout2 = go.Layout(title='Total Medals in Winter Olympics 2018 (Nested Bar Chart)',
                    xaxis={'title':'Countries'}, #can use {} approach
                    yaxis=dict(title='Medals'),
                    barmode='stack') #can use dict also

fig2 =go.Figure(data=data1,layout=layout2)
pyo.plot(fig2,filename='Bar-Chart-Stacked.html')

#----------------------------------------------------------------------------------------#
