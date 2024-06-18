# Import the stockvalues.csv file.
# The data is for dates, high, open and low values for a stock.
# Use the dates list for X-axes and use the high, open and low for y axes.
# Then draw a 3x2 grid of charts and display the lines for high, open and low in three of the boxes in the 3x2 grid.

import matplotlib.pyplot as plt
from matplotlib import style
import csv

stock_high = []
stock_low = []
stock_open = []
date = []

file_handle = open('stockvalues.csv','r')
csvdata = csv.reader(file_handle)
csv_list = list(csvdata)
# print (csv_list)

#print (csv_list[2][0])
# #get data fom the csv lists and put them into our data lists

for elem in csv_list:
    print(elem)
    date.append(elem[0])
    stock_high.append(float(elem[1]))
    stock_open.append(float(elem[2]))
    stock_low.append(float(elem[3]))
file_handle.close()
# print(date)
# print (date)
# style.use ('ggplot')
# # fig1 = plt.figure(1)
# plt.subplot(3,1,1)
# line1 = plt.plot(date, stock_high,
#                  color = 'green',
#                  linestyle = 'dashed',
#                  marker = 's',
#                  linewidth = 3,
#                  label = 'Stock High'
#                  )
# plt.legend()
# plt.xlabel ('Value')
# plt.ylabel ("Date")
# # plt.title ('Majors vs Number of students')
# plt.subplot(312)
# line2 = plt.plot(date, stock_open,
#                  color = 'red',
#                  linestyle = '-',
#                  marker = 'o',
#                  linewidth = 2,
#                  label = 'Stock Open'
#                  )
# plt.xlabel ('Value')
# plt.ylabel ("Date")
# #plt.title ('Majors vs Number of women')
# plt.legend()
#
# plt.subplot(3,1,3)
# line3 = plt.plot(date, stock_low,
#                  color = 'yellow',
#                  linestyle = '-',
#                  marker = 'v',
#                  linewidth = 2,
#                  label = 'Stock Low'
#                  )
# plt.legend()
# plt.xlabel ('Value')
# plt.ylabel ("Date")
# plt.subplot(3,1,3)
# line4 = plt.plot(date, stock_low,
#                  color = 'yellow',
#                  linestyle = '-',
#                  marker = 'v',
#                  linewidth = 2,
#                  label = 'Stock Low'
#                  )
# plt.legend()
# plt.xlabel ('Value')
# plt.ylabel ("Date")
#
#
# plt.show()