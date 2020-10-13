# In this script, we will analyze Heatmaps using plotly functions

import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

#dataset read

df = pd.read_csv('2010SantaBarbaraCA.csv')

# Heatmap data
data = [go.Heatmap(x=df['DAY'], #x - xaxis, y- yaxis and z- color axis
                   y=df['LST_TIME'],
                   z=df['T_HR_AVG'].values.tolist())] # for color axis, we need a lsit so we convert with .values.tolist() from column to list

layout = go.Layout(title='Heatmap for Temperature in Santa Barbara 2010') 

fig=go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Basic-Heatmap-Temps.html')

#-------------------------------------------------------------------------------------------------------------------------------------------------#

#Different color scales

data1 = [go.Heatmap(x=df['DAY'], #x - xaxis, y- yaxis and z- color axis
                   y=df['LST_TIME'],
                   z=df['T_HR_AVG'].values.tolist(),
                   colorscale='Jet')] 

layout1 = go.Layout(title='Heatmap for Temperature in Santa Barbara 2010 - Jet colormap') 

fig1=go.Figure(data=data1,layout=layout1)
pyo.plot(fig1,filename='Colormaps-Heatmap-Temps.html')

#------------------------------------------------------------------------------------------------#

# Multiple heatmaps on one plot (subplot)

df1 = pd.read_csv('2010SitkaAK.csv')
df2 = pd.read_csv('2010SantaBarbaraCA.csv')
df3 = pd.read_csv('2010YumaAZ.csv')

# trace for each heatmap

trace1 = go.Heatmap(x=df1['DAY'],
                    y=df1['LST_TIME'],
                    z=df1['T_HR_AVG'].values.tolist(),
                    colorscale='Jet',zmin=5,zmax=40)
trace2 = go.Heatmap(x=df2['DAY'],
                    y=df2['LST_TIME'],
                    z=df2['T_HR_AVG'].values.tolist(),
                    colorscale='Jet',zmin=5,zmax=40)
trace3 = go.Heatmap(x=df3['DAY'],
                    y=df3['LST_TIME'],
                    z=df3['T_HR_AVG'].values.tolist(),
                    colorscale='Jet',zmin=5,zmax=40)

from plotly import tools

figx = tools.make_subplots(rows=1,cols=3, #rows and columns (horiztonal or vertical stacking)
                          subplot_titles=['Sitka AK', 'SB CA', 'Yuma AZ'],
                          shared_yaxes=False) #same time stamp for all 3 data, so we keep separte ones

# allotment of heatmap in rows and columns
figx.append_trace(trace1,1,1)
figx.append_trace(trace2,1,2)
figx.append_trace(trace3,1,3)

figx['layout'].update(title='Temps for 3 cities') # to add title for mulitple heatmaps in one plot

pyo.plot(figx,filename='Mutiple-Heatmap-Temps.html')

