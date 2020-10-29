# In this program we will make dash components (HTML and core) interactive using @callbacks

# In this program we will use graphs and make them interactive using callback only

import dash  
import dash_core_components as dcc  
import dash_html_components as html 

from dash.dependencies import Input,Output

import plotly.graph_objs as go 
import pandas as pd

#Read dataset
df = pd.read_csv('gapminderDataFiveYear.csv')

app = dash.Dash()

year_options=[] #for dropdown
for year in df['year'].unique():
    year_options.append({'label':str(year),'value':year}) #year label and value

app.layout = html.Div([
            dcc.Graph(id='graph'),
            dcc.Dropdown(id='year-picker',
                         options=year_options,
                         value=df['year'].min())
])


# Now if we use callbacks we can make our above core component interactive 

#for decoration
@app.callback(Output(component_id='graph', #Output - graph
                     component_property='figure'), #figure
                     [Input(component_id='year-picker', #Input - year
                     component_property='value')]) 


def update_figure(selected_year): #return updated figure
    filtered_df = df[df['year']==selected_year] #Data selected only for a particular year

    traces = [] #traces ofr every continent for a specific year
    for continent_name in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent']==continent_name] #from filtered data choose the continent
        traces.append(go.Scatter( #Scatter plot
            x = df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            mode='markers', 
            opacity=0.7,
            marker = {'size':15},
            name=continent_name
        ))
    return {'data':traces,
            'layout': go.Layout(title='My plot',
                                xaxis={'title':'GDP per Cap','type':'log'},
                                yaxis={'title':'Life Expectancy'})}

if __name__ == "__main__":
    app.run_server()
