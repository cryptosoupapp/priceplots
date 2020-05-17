#>>> import bokeh.sampledata
#>>> bokeh.sampledata.download()
 
#Importing the necessary modules and tools
import numpy as np
 
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT
 
#Function for converting dates to the proper format
def datetime(x):
    return np.array(x, dtype = np.datetime64)
 
#Creating a new plot with various optional parameters
p = figure(x_axis_type = "datetime", title = "Stock Prices")
 
#Setting other optional parameters
p.grid.grid_line_alpha = 0.3
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Price'
 
#Converting dates to the proper format and drawing the lines
p.line(datetime(AAPL['date']), AAPL['adj_close'], color = '#A6CEE3', legend_label = 'AAPL')
p.line(datetime(GOOG['date']), GOOG['adj_close'], color = '#B2DF8A', legend_label = 'GOOG')
p.line(datetime(IBM['date']), IBM['adj_close'], color = '#33A02C', legend_label = 'IBM')
p.line(datetime(MSFT['date']), MSFT['adj_close'], color = '#FB9A99', legend_label = 'MSFT')
 
#Setting the location of the legend on the plot
p.legend.location = "top_left"
 
#Creating the output HTML file in the current folder
output_file("stocks.html", title = "Stocks Comparison")
 
#Displaying the final result
show(p)