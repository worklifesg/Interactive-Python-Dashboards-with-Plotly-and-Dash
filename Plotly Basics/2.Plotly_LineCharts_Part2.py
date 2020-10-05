# In this script, we will analyze line charts using plotly functions (on some real data)

import numpy as np
import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objs as go 

df = pd.read_csv('nst-est2017-alldata.csv')

print(df.head())

#filtering some data (grab only some 6 New England states)

df2 = df[df['DIVISION'] =='1']
df2.set_index('NAME',inplace=True) #grab that column in df and set index

list_of_pop_col = [col for col in df2.columns if col.startswith('POP')] #choosing population estimate columns
df2 = df2[list_of_pop_col]

data = [go.Scatter(x=df2.columns, # every column i.e. year 
        y=df2.loc[name], #for every column grab the corresponding estimate value (y) for each state
        mode='lines',
        name=name) for name in df2.index]

layout = go.Layout(title='Population estimate Plot',
                    xaxis={'title':'2011-2017'}, #can use {} approach
                    yaxis=dict(title='Population estimate'), #can use dict also
                    hovermode='closest') #handle multiple points on the same data (both x and y)

fig =go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Population-estimate-plot.html')

#--------------------------------------------------------------------------------------------------------------#

