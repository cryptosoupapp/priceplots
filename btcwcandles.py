#Importing the necessary modules and tools
from math import pi
 
import pandas
 
from bokeh.plotting import figure, show, output_file
 
#Reading the HTML data into a Pandas dataframe
df = pandas.read_html("https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20190220&end=20190320")[2][::-1]
 
#Converting the Date column to the proper datetime format
#e.g. from "Mar 20, 2019" to "2019-03-20"
df["Date"] = pandas.to_datetime(df["Date"])
 
#Renaming the columns to eliminate any issues caused by the asterisk(s)
df.rename(index = str, columns = {"Open*": "Open"}, inplace = True)
df.rename(index = str, columns = {"Close**": "Close"}, inplace = True)
 
#Comparing the Open and Close daily prices to set the candle color
inc = df.Close > df.Open
dec = df.Open > df.Close
 
#Setting the width of each candlestick to half a day (in milliseconds)
w = 12 * 60 * 60 * 1000
 
#Defining the optional interactive tools for the plot
tools = "pan,wheel_zoom,box_zoom,reset,save"
 
#Creating a new plot with various optional parameters
p = figure(x_axis_type = "datetime", tools = tools, plot_width = 1200, title = "Bitcoin Candlesticks")
 
#Setting other optional parameters for visual styling
p.xaxis.major_label_orientation = pi / 4
 
p.grid.grid_line_alpha = 0.3
 
#Drawing the vertical bars (candlesticks) and setting visual properties
#segment: https://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.figure.Figure.segment
p.segment(df.Date, df.High, df.Date, df.Low, color = "black")
 
p.vbar(df.Date[inc], w, df.Open[inc], df.Close[inc], fill_color = "#D5E1DD", line_color = "black")
 
p.vbar(df.Date[dec], w, df.Open[dec], df.Close[dec], fill_color = "#F2583E", line_color = "black")
 
#Creating the output HTML file in the current folder
output_file("bitcoin.html", title = "Bitcoin Candlesticks")
 
#Displaying the final result
show(p)