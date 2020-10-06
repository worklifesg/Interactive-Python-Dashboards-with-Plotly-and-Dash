#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:

import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objs as go 


# create a DataFrame from the .csv file:

df = pd.read_csv('mocksurvey.csv',index_col=0) # bit trick as index column is not set
print(df.head())
# create traces using a list comprehension:

trace1 = go.Bar(x=df.index,
                y=df['Strongly Agree'],
                name='Strongly Agree')

trace2 = go.Bar(x=df.index,
                y=df['Somewhat Agree'],
                name='Somewhat Agree')

trace3 = go.Bar(x=df.index,
                y=df['Neutral'],
                name='Neutral')

trace4 = go.Bar(x=df.index,
                y=df['Somewhat Disagree'],
                name='Somewhat Disagree')

trace5 = go.Bar(x=df.index,
                y=df['Strongly Disagree'],
                name='Strongly Disagree') 

data = [trace1,trace2,trace3,trace4,trace5]

layout = go.Layout(title='Survey Response',
                    xaxis={'title':'Questions'}, #can use {} approach
                    yaxis=dict(title='Count'),
                    barmode='stack') #to make it stacked bar chart

fig =go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='StackedBarChart_Vertical.html')

#-------------------------------------------------------------------------

# Another way to do stacked bar chart is using for loop (easy) and we will see hor horizontal bar chart

data1 = [go.Bar(y=df.index,
                x=df[response],
                orientation='h',
                name=response) for response in df.columns]
layout1 = go.Layout(
    title='Mock Survey Results',
    barmode='stack'
)
fig1 =go.Figure(data=data1,layout=layout1)
pyo.plot(fig1,filename='StackedBarChart_Horizontal.html')


#-------------------------------------------------------------------------------------------------#
