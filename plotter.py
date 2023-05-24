import pandas as pd
import csv 
import matplotlib.pyplot as plt
import numpy as np

def plotter(filename,col1,col2,fit):
    if fit == True:
        fh = open(filename)
        csvread = csv.reader(fh)
        csvhead = next(csvread)
        values = pd.read_csv(filename, header = None, skiprows = 2, names = csvhead)
        x = values[col1]
        y = values[col2]
        plt.plot(x,y)
        a, b = np.polyfit(x, y,1)
        plt.scatter(x,a*(x)+b)
        fh.close()
    else:
        fh = open(filename)
        csvread = csv.reader(fh)
        csvhead = next(csvread)
        values = pd.read_csv(filename, header = None, skiprows = 2, names = csvhead)
        values.plot()
        fh.close()


        