import random
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
import numpy as np
import csv

file = open("sim1Data.txt", "r")
csvreader = csv.reader(file)
data = []
for row in csvreader:
    for item in row:
        data.append(int(item))
histdata = []
for datum in enumerate(data):
    histdata.append(datum[0])
    histdata.append(datum[1])
hist = np.histogram(histdata, bins = 5, range=[15, 45])
yvals = hist[0]
xvals = hist[1]
xbarwidth = 5

h = figure(title = "Frequency of Times Taken to Infect Entire Populations Completely Random (Sim 1)", x_axis_label = "Time Taken to Infect Entire Population", y_axis_label = "Number of Trials with Time")
for x, y in zip(xvals, yvals):
    h.vbar(x, xbarwidth, y)
file = open("sim2Data.txt", "r")
csvreader2 = csv.reader(file)
data2 = []
for row in csvreader2:
    for item in row:
        data2.append(int(item))
histdata2 = []
for datum in enumerate(data2):
    histdata2.append(datum[0])
    histdata2.append(datum[1])
hist = np.histogram(histdata2, bins = 5, range=[15, 40])
yvals = hist[0]
xvals = hist[1]
xbarwidth = 4

f = figure(title = "Frequency of Times Taken to Infect Entire Populations with Chasing (Sim 2)", x_axis_label = "Time Taken to Infect Entire Population", y_axis_label = "Number of Trials with Time")
for x, y in zip(xvals, yvals):
    f.vbar(x, xbarwidth, y)
file = open("sim3Data.txt", "r")
csvreader3 = csv.reader(file)
data3 = []
for row in csvreader3:
    for item in row:
        data3.append(int(item))
histdata3 = []
for datum in enumerate(data3):
    histdata3.append(datum[0])
    histdata3.append(datum[1])
hist = np.histogram(histdata3, bins = 10, range=[48, 290])
yvals = hist[0]
xvals = hist[1]
xbarwidth = 20

p = figure(title = "Frequency of Times Taken to Infect Entire Populations with Covid Sim (Sim 3)", x_axis_label = "Time Taken to Infect Entire Population", y_axis_label = "Number of Trials with Time")
for x, y in zip(xvals, yvals):
    p.vbar(x, xbarwidth, y)
z = gridplot([[h, f], [p]])
show(z)