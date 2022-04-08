#plottask.py
# This program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes
# Author Michael Casey

#import numpy and matplotlip

import numpy as np
import matplotlib.pyplot as plt

#import more styling options - matplotlib - https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html
from matplotlib import style

#specifying the style to apply to the chart - source https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html
style.use('ggplot')


#setting the range
xpoints = np.array(range(0,4))
#establishing the functions and calculating the values to be include for each of the 3 y values
fx = xpoints
gx = xpoints * xpoints
hx = xpoints * xpoints * xpoints

#plotting each of the three values, assigning labels to each plot and an associated line color
plt.plot(xpoints, fx, label = "f(x)", color = "red")
plt.plot(xpoints, gx, label = "g(x)", color = "green")
plt.plot(xpoints, hx, label = "h(x)", color = "blue")

#putting a title on the plot
plt.title("Weekly Task 8 - Plot Task")
#adding a legend to the plot area
plt.legend()
#adding a grid to the plot 
plt.grid()
#Displaying plot
plt.show()


