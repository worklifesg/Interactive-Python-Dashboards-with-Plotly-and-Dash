## Interactive-Python-Dashboards-with-Plotly-and-Dash

In this repository, we will work on interactive plots using Plotly and Dasboards using dash.

![1](https://img.shields.io/badge/Python-v%203.8.3-green) ![2](https://img.shields.io/badge/plotly-v%204.11.0-blue) ![3](https://img.shields.io/badge/dash-v%201.16.2-red) ![4](https://img.shields.io/badge/numpy-v%201.19.1-orange) ![5](https://img.shields.io/badge/pandas-v%201.0.5-orange)

### Programs

* Plotly Scatter Plot - [Scatter Plot Code](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Plotly%20Basics/1_Scatter_Plots.py), [Results 1](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/scatter-plot.html), [Results 2](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/scatter-plot-modified.html)
  ```
  go.Scatter, go.Layout, go.Figure
  ```
* Plotly Line Charts - [Line Chart Code](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Plotly%20Basics/2_Line_Charts_Part1.py), Results - [Markers only](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Line-Chart.html), [Lines Only](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Line-Chart-with%20lines.html), [Lines + Markers](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Line-Chart-with-lines-markers.html)
  ```
  go.Scatter(mode='lines','markers','lines+markers'), go.Layout, go.Figure
  data = [trace0, trace1, ....], can combine all graphs in one data list.
  ```
    * Line Charts on real data - [Code](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Plotly%20Basics/2.Plotly_LineCharts_Part2.py), [Dataset](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Datasets/nst-est2017-alldata.csv), [Result-Lines](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Population-estimate-plot.html)
    * Exercise - [Code Solution](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Plotly%20Basics/Exercise1_LineChart.py), [Dataset](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Datasets/2010YumaAZ.csv), [Solution](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Daily-Temperature-Yuma-2010.html)

* Plotly Bar Charts - [Bar Chart Code](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Plotly%20Basics/3.Plotly_BarCharts.py), [Dataset](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Datasets/2018WinterOlympics.csv), Results - [Simple Bar Chart](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Bar-Chart-Simple.html), [Nested Bar Chart](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Bar-Chart-Nested.html), [Stacked Bar Chart](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Bar-Chart-Stacked.html)
  ```
  go.Bar(x=df['NOC'],
        y=df['Gold'],
        name='Gold',
        marker={'color':'#FFD700'}), go.Layout, go.Figure
  data = [trace0, trace1, ....], can produce nested and stacked bar charts
  ```
    * Exercise - [Code Solution](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Plotly%20Basics/Exercise2_Barchart.py), [Dataset](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Datasets/mocksurvey.csv), [Solution_Vertical_Stacked_BarChart](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/StackedBarChart_Vertical.html), [Solution_Horizontal_Stacked_BarChart](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/StackedBarChart_Horizontal.html)

* Plotly Bubble Charts - [Bubble Chart Code](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Plotly%20Basics/4.Plotly_BubbleCharts.py), [Dataset](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Datasets/mpg.csv), Results - [MPG-HP-cylinders](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Bubble-Chart-cylinders.html), [MPG-HP-weight](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Bubble-Chart-weight.html), [MPG-HP-weight-cylinders](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Bubble-Chart-categorical.html)
  ```
  [go.Scatter(x=df['horsepower'],
                    y=df['mpg'],
                    text = df['name'], #text for hovering
                    mode = 'markers', 
                    marker=dict(size=0.01*df['weight'],color=df['cylinders'], #adding cylinders as categorical features 
                    showscale=True))] # showscale to no. of cylinders on its scale
  ```
