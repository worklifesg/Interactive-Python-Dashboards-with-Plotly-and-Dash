## Project: Milestone (Stock Ticker Dashboard)


![1](https://img.shields.io/badge/Python-v%203.8.3-green) ![2](https://img.shields.io/badge/plotly-v%204.11.0-blue) ![3](https://img.shields.io/badge/dash-v%201.16.2-red) ![4](https://img.shields.io/badge/numpy-v%201.19.1-orange) ![5](https://img.shields.io/badge/pandas-v%201.0.5-orange) ![6](https://img.shields.io/badge/pandas--datareader-v%200.9.0-orange) 

The goal of this project is to develop a dashboard that allows users to select one or more stocks, a start and end date, and have the closing stock prices displayed as a time series.
Rather than attempt to code it all at once, we’ll break it down into manageable (and testable) benchmarks.

The sequence of tasks will be:
```
Task 1 - Perform imports, set up a graph with static data, ensure that we can lay everything out on the screen
Task 2 - Add an input box and a basic callback to display the input value (the ticker) on the graph. 
Task 3 - Ensure that we can read data off the web using pandas datareader
Task 4 - Add datepickers to select start and end dates and apply them to the callback
Task 5 - Take advantage of Dash State, and hold all API calls until a Submit button is pressed
Task 6 - Replace the input box with a multiple dropdown list of choices. Pass multiple stocks as traces on the same graph.
```

### Sequence Code Development

* **Task 1** - In the first task of the code, we import libraries and set up static graph along with headers for giving out title of the dashboard

  ***For importing libraries intially***:
  ```javascript
  import dash 
  import dash_core_components as dcc
  import dash_html_components as html 
  ```
  ***Defining the dashboard app:***
  ```javascript
  app = dash.Dash()
  ```
  ***For title headers and setting up static graph for TSLA in app layout***
  ```javascript
  app.layout = html.Div([
                  html.H1('Stock Ticker DashBoard'),
                  html.H3('Enter a stock symbol: '),
                  dcc.Input(id='my_stock_picker',
                          value='TSLA'),
                  dcc.Graph(id='my_graph',
                          figure={'data':[{'x':[1,2],'y':[3,1]}
                            ]}
  ```
  ***Executing the program by run_server()***
  ```javascript
  if __name__ == "__main__":
      app.run_server()
  ```
***Task 1 Output*** 
<p align="center">
  <img width="950" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/images/Task1.PNG">
</p>

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

* **Task 2** - Add an input box and a basic callback to display the input value (the ticker) on the graph.

  Few changes to Task 1: 
  ***First we add layout with Default title to app.layout***
  ```javascript
  app.layout = html.Div([
                html.H1('Stock Ticker DashBoard'),
                html.H3('Enter a stock symbol: '),
                dcc.Input(id='my_stock_picker',
                          value='TSLA'),
                dcc.Graph(id='my_graph',
                          figure={'data':[{'x':[1,2],'y':[3,1]}
                          ],'layout':{'title':'Default Title'}} # We add default title in Task 1 Code
                )
  ])
  ```
  ***Then we create callbacks for stock picker and graph associated with it***
  ```javascript
  from dash.dependencies import Input,Output
  @app.callback(Output('my_graph','figure'),
              [Input('my_stock_picker','value')])
  ```
  ***Callbacks function to return the figure***
  ```javascript
  def update_graph(stock_ticker):
     fig = {'data':[{'x':[1,2],'y':[3,1]}],
            'layout':{'title':stock_ticker}
     }
     return fig
  ```
***Task 2 Output*** 

![Alt Text](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/images/Task2a.gif)


**Note:** - The project covered in the course used [IEX (Investors Exchange)](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-iex) which had free access before 1 June, 2019 and now requires an API key from IEX Cloud Console, which can be stored in the IEX_API_KEY environment variable. To use this key we need to create account and upgrade to premium account to access the data. So we will be **NOT** using IEX data for our project

***Therefore, we will use STOOQ data which is an open source for Indices across Asia, Americas, Europe, and Middle East***

* **Task 3** - Ensure that we can read data off the web using pandas datareader

  Few changes to Task 2 callback return function where we use pandas-datareader to get latest data from STOOQ: 
  ***Callbacks function to return the figure***
  ```javascript
   def update_graph(stock_ticker):

     start = datetime(2020,1,1) #1 Jan 2017 start date
     end = datetime(2020,10,31) #31 Dec 2017 end date
     df = web.DataReader(stock_ticker,'stooq',start,end)
     fig = {'data':[{'x':df.index,'y':df.Close}],
             'layout':{'title':stock_ticker}}
     return fig
  ```
***Task 3 Output*** 

<p align="center">
  <img src="https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/images/Task3.gif" />
</p>

***Now we modified the layout according to the data provided by STOOQ. As the data is segmented into indices from different continents, so we segmented the graphs into four graphs for each region specifically***

  Changes made in the code are:
  
  ***Changes in app.layout***
  ```javascript
  app.layout = html.Div([
            html.Div([
                html.H1('Stock Ticker DashBoard'),
                html.H2('Asia Indices'),
                html.H3('Enter a stock symbol: '),
                dcc.Input(id='my_stock_picker',
                          value='^SNX'),
                dcc.Graph(id='my_graph',
                          figure={'data':[{'x':[1,2],'y':[3,1]},
                          ],'layout':{'title':'Default Title'}} 
                )
],style={'width':'48%','display':'inline-block'}),
            html.Div([html.H2('America Indices'),
                html.H3('Enter a stock symbol: '),
                dcc.Input(id='my_stock_picker2',
                          value='^SPX'),
                dcc.Graph(id='my_graph2',
                          figure={'data':[{'x':[1,2],'y':[3,1]}
                          ],'layout':{'title':'Default Title'}}
                ),

],style={'width':'48%','display':'inline-block'}),
            html.Div([html.H2('Europe Indices'),
                html.H3('Enter a stock symbol: '),
                dcc.Input(id='my_stock_picker3',
                          value='^PX'),
                dcc.Graph(id='my_graph3',
                          figure={'data':[{'x':[1,2],'y':[3,1]}
                          ],'layout':{'title':'Default Title'}} 
                ),

],style={'width':'48%','display':'inline-block'}),
            html.Div([html.H2('Middle East Indices'),
                html.H3('Enter a stock symbol: '),
                dcc.Input(id='my_stock_picker4',
                          value='^TASI'),
                dcc.Graph(id='my_graph4',
                          figure={'data':[{'x':[1,2],'y':[3,1]}
                          ],'layout':{'title':'Default Title'}} 
                ),

],style={'width':'48%','display':'inline-block'})
])
```
  ***Changes in callbacks***
  ```javascript
  @app.callback(Output('my_graph','figure'),
              [Input('my_stock_picker','value')])
def update_graph(stock_ticker):
    start = datetime(2020,1,1) 
    end = datetime(2020,10,31) 
    df = web.DataReader(stock_ticker,'stooq',start,end)
    fig = {'data':[{'x':df.index,'y':df.Close}],
            'layout':{'title':stock_ticker}}
    return fig


@app.callback(Output('my_graph2','figure'),
              [Input('my_stock_picker2','value')])
def update_graph(stock_ticker2):
    start = datetime(2020,1,1) 
    end = datetime(2020,10,31) 
    df = web.DataReader(stock_ticker2,'stooq',start,end)
    fig = {'data':[{'x':df.index,'y':df.Close}],
            'layout':{'title':stock_ticker2}}
    return fig

@app.callback(Output('my_graph3','figure'),
              [Input('my_stock_picker3','value')])
def update_graph(stock_ticker3):
    start = datetime(2020,1,1) 
    end = datetime(2020,10,31) 
    df = web.DataReader(stock_ticker3,'stooq',start,end)
    fig = {'data':[{'x':df.index,'y':df.Close}],
            'layout':{'title':stock_ticker3}}
    return fig

@app.callback(Output('my_graph4','figure'),
              [Input('my_stock_picker4','value')])
def update_graph(stock_ticker4):
    start = datetime(2020,1,1) 
    end = datetime(2020,10,31) 
    df = web.DataReader(stock_ticker4,'stooq',start,end)
    fig = {'data':[{'x':df.index,'y':df.Close}],
            'layout':{'title':stock_ticker4}}
    return fig
  ```

***Modified Task 3 Output*** 

<p align="center">
  <img src="https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/images/Task3a.gif" />
</p>
