import numpy as np
import matplotlib.pyplot as plt

def line_chart_with_lineobject():
    #lines = plt.plot(x1, y1, x2, y2)
    line = plt.plot([1,2,3,4],[1,4,9,16])
    plt.setp(line, color='r', linewidth = 2.0)
    plt.show()
    print("x points: ", line.get_xdata(), "y points : ", line.get_ydata())
    return()

line_chart_with_lineobject()
