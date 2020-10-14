## Interactive-Python-Dashboards-with-Plotly-and-Dash

In this repository, we will work on interactive plots using Plotly and Dasboards using dash.

![1](https://img.shields.io/badge/Python-v%203.8.3-green) ![2](https://img.shields.io/badge/plotly-v%204.11.0-blue) ![3](https://img.shields.io/badge/dash-v%201.16.2-red) ![4](https://img.shields.io/badge/numpy-v%201.19.1-orange) ![5](https://img.shields.io/badge/pandas-v%201.0.5-orange)

### Notes
  1. [Plotly Basics](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Plotly_Notes.pdf) - Scatter Plots, Line Charts, Bar Charts, Bubble Charts, Box Plots, Histograms, DistPlots, and Heatmaps
  
### Programs & Exercises (Plotly)

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
    * Exercise - [Code Solution](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Plotly%20Basics/Exercise3_Bubblechart.py), [Dataset](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Datasets/mpg.csv), [Solution_Bubble Chart - 4 Features](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Bubble-Chart-Exercise.html)
    
* Plotly Box Plots - [Box Plot Code](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Plotly%20Basics/5.Plotly_BoxPlots.py), Results - [Simple Box plot](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Simple-Box-Plot.html), [Outliers Box plot](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Outliers-Box-Plot.html), [Snodgrass-Twain Box Plot](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Snodgrass-Twain-Box-Plot.html)
  ```
  data =[go.Box(y=y,  #No categorical x column
        boxpoints='all', #boxpoints, displays all original data points
        jitter=0.3, #spread all values properly 
        pointpos=2)]  #offset points to left (-ve) or right (+ve)
  ```
    * Exercise - [Code Solution](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Plotly%20Basics/Exercise4_BoxPlot.py), [Solution_Box Plot](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Box-Plot-Exercise.html)

* Plotly Histogram Plots - [Histogram Plot Code](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Plotly%20Basics/6.Plotly_HistogramPlots.py), Results - [Simple Histogram plot](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Simple-Histogram-Plot.html), [Wide bins Histogram plot](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Modified-Histogram-Plot.html), [Narrower bins Histogram plot](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Modified2-Histogram-Plot.html)
  ```

  data2 = go.Histogram(x=df['mpg'],
                    xbins=dict(start=0,end=50,size=1)) #display histogram from 0 to 50 mpg with each bin of 1 mpg
  ```
    * Exercise - [Code Solution](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Plotly%20Basics/Exercise5_HistogramPlot.py), [Dataset](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Datasets/abalone.csv), [Solution_Histogram Plot](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Histogram-Plot-Exercise.html)
    

* Plotly Distribution Plots (DistPlot) - [DistPlot Code](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Plotly%20Basics/7.Plotly_DistPlots.py), Results - [Basic DistPlot](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Basic-Distplot.html), [Multigroup DistPlot](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Multigroup-Distplot.html), [Multigroup Binsize DistPlot](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Multigroup-Distplot-BinSize.html), [Snodgrass-Twain DistPlot](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/SnodgrassTwain-Distplot.html)
  ```

  hist_data = [x] #list of data points
  group_labels=['Distplot'] #labels

  fig2=ff.create_distplot(hist_data,group_labels=group_labels, bin_size=[0.2,0.1,0.3,0.4]) # using ff.create
  ```
    * Exercise - [Code Solution](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Plotly%20Basics/Exercise6_Distplot.py), [Dataset](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Datasets/iris.csv), [Solution_DistPlot](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Iris-DistPlot.html)
    
* Plotly Heatmaps - [Heatmap Code](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Plotly%20Basics/8.Plotly_Heatmaps.py), Dataset - [Sitka AK](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Datasets/2010SitkaAK.csv), [Santa Barbara CA](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Datasets/2010SantaBarbaraCA.csv), [Yuma AZ](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Datasets/2010YumaAZ.csv), Results - [Basic Heatmaps](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Basic-Heatmap-Temps.html), [ColorMaps Heatmaps](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Colormaps-Heatmap-Temps.html), [Multiple Heatmaps](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Mutiple-Heatmap-Temps.html)
  ```

  data = [go.Heatmap(x=df['DAY'], #x - xaxis, y- yaxis and z- color axis
                   y=df['LST_TIME'],
                   z=df['T_HR_AVG'].values.tolist())] # for color axis, we need a lsit so we convert with .values.tolist() from column to list
                   
  For multiple plots:
  
    
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
  
  
  ```
    * Exercise - [Code Solution](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Plotly%20Basics/Exercise7_Heatmaps.py), [Dataset](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Datasets/flights.csv), [Solution_Heatmaps Flights](https://worklifesg.github.io/Interactive-Python-Dashboards-with-Plotly-and-Dash/Heatmap-Exercise-Flights.html)

### Program & Exercises (Dash)
* Dash Basics - [Hello Dash Code](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Dash/1.Dash_Basic.py)

<p align="center">
  <img width="600" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/images/Dash_Basic.PNG">
</p> 

* Dash Basics (HTML components - Div) - [Code](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Dash/1.Dash_Basic2.py)

<p align="center">
  <img width="600" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/images/Dash_Basic2.PNG">
</p> 

* Dash Basics (HTML + Core components) - [Code](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Dash/1.Dash_Basic3.py)

<p align="center">
  <img width="600" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/images/Dash_Basic3.PNG">
</p> 

* Dash Basics (HTML + Core components+Style) - [Code](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Dash/2.Dash_Basic_Styles.py)

<p align="center">
  <img width="600" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/images/Dash_Basic_Styles.PNG">
</p>

* Dash + Plotly (Basics) - [Code](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Dash/3.Dash_Plotly.py)

<p align="center">
  <img width="600" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/images/Dash_Plotly_1.PNG">
</p> 


* Dash + Plotly (Advanced) - [Code](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Dash/3.Dash_Plotly2.py)

<p align="center">
  <img width="600" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/images/Dash_Plotly_2.PNG">
</p> 

* Dash + Plotly (Multiple plots) - [Code](https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/Dash/3.Dash_Plotly3.py)

<p align="center">
  <img width="600" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Interactive-Python-Dashboards-with-Plotly-and-Dash/blob/main/images/Dash_Plotly_3.PNG">
</p> 
