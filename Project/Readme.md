### Project: Milestone


![1](https://img.shields.io/badge/Python-v%203.8.3-green) ![2](https://img.shields.io/badge/plotly-v%204.11.0-blue) ![3](https://img.shields.io/badge/dash-v%201.16.2-red) ![4](https://img.shields.io/badge/numpy-v%201.19.1-orange) ![5](https://img.shields.io/badge/pandas-v%201.0.5-orange)

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
