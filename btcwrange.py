#Importing the necessary modules and tools
import pandas
 
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, RangeTool
from bokeh.plotting import figure, output_file, show
 
#Reading the HTML data into a Pandas dataframe
df = pandas.read_html("https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20190220&end=20190320")[2][::-1]
 
#Converting the Date column to the proper datetime format
#e.g. from "Mar 20, 2019" to "2019-03-20"
df["Date"] = pandas.to_datetime(df["Date"])
 
#Converting the Date column to a NumPy array
dates = df["Date"].to_numpy(dtype = 'datetime64[D]')
 
#At the most basic level, a ColumnDataSource is simply a mapping between column names and lists of data.
#The ColumnDataSource takes a data parameter which is a dict, 
#with string column names as keys and lists (or arrays) of data values as values. 
#If one positional argument is passed in to the ColumnDataSource initializer, it will be taken as data.
#Once the ColumnDataSource has been created, it can be passed into the source parameter of plotting methods
#which allows you to pass a column’s name as a stand in for the data values
#Source: https://bokeh.pydata.org/en/latest/docs/user_guide/data.html#columndatasource
source = ColumnDataSource(data = dict(date = dates, close = list(df['Close**'])))
 
#Creating a new plot with various optional parameters
p = figure(plot_height = 300, plot_width = 1200, tools = "", toolbar_location = None,
           x_axis_type = "datetime", x_axis_location = "above",
           background_fill_color = "#efefef", x_range=(dates[12], dates[20]))
 
#Drawing the line
p.line('date', 'close', source = source)
 
#Naming the y axis
p.yaxis.axis_label = 'Price'
 
#Creating a new plot (the once containing the range tool) with various optional parameters
select = figure(title = "Drag the middle and edges of the selection box to change the range above",
                plot_height = 130, plot_width = 1200, y_range = p.y_range,
                x_axis_type = "datetime", y_axis_type = None,
                tools = "", toolbar_location = None, background_fill_color = "#efefef")
 
#Creating the range tool - setting the default range
range_tool = RangeTool(x_range = p.x_range)
 
#Setting other optional parameters
range_tool.overlay.fill_color = "navy"
range_tool.overlay.fill_alpha = 0.2
 
#Drawing the line and setting additional parameters
select.line('date', 'close', source = source)
select.ygrid.grid_line_color = None
select.add_tools(range_tool)
select.toolbar.active_multi = range_tool
 
#Creating the output HTML file in the current folder
output_file("btc_range.html", title = "Bitcoin Price Chart")
 
#Displaying the final result
show(column(p, select))
