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

print(csv_list[2][0])
print(csv_list[0])
# # #get data fom the csv lists and put them into our data lists
#
# for elem in csv_list:
#     # print(elem)
#     date.append(csv_list[0])
#     stock_high.append(float(elem) for elem in csv_list[2])
#     stock_open.append(float(elem) for elem in csv_list[1])
#     stock_low.append(float(elem) for elem in csv_list[3])

date = csv_list[0]  # The first row contains the dates
stock_high = [float(value) for value in csv_list[2]]  # The second row contains the stock high values
stock_low = [float(value) for value in csv_list[1]]   # The third row contains the stock low values
stock_open = [float(value) for value in csv_list[3]]  # The fourth row contains the stock open values
file_handle.close()
#
style.use ('ggplot')

plt.xlabel ('Date')
plt.ylabel ("Stock Value")
# plt.title ('Majors vs Number of students')
plt.subplot(3,1,1)
line2 = plt.plot(date, stock_open, color = 'black', linestyle = '--', marker = '*', linewidth = 2,
                 label = 'Stock Open')
plt.xlabel ('Date')
plt.ylabel ("Stock Value")
plt.title ('Stock Values Over Time')
plt.legend()

plt.subplot(3,1,2)
line1 = plt.plot(date, stock_high, color = 'green', linestyle = '--', marker = '*', linewidth = 3,
                 label = 'Stock High')
plt.xlabel ('Date')
plt.ylabel ("Stock Value")
plt.legend()

plt.subplot(3,1,3)
line3 = plt.plot(date, stock_low, color = 'red', linestyle = '--', marker = '*', linewidth = 2,
                 label = 'Stock Low')
plt.legend()
plt.xlabel ('Date')
plt.ylabel ("Stock Value")
plt.show()