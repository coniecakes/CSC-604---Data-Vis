import matplotlib.pyplot as plt
import csv

stock_high = []
stock_low = []
stock_open = []
date = []

# Read the CSV file
file_path = 'stockvalues.csv'
with open(file_path, 'r') as file_handle:
    csvdata = csv.reader(file_handle)
    csv_list = list(csvdata)

# Extract the data
date = csv_list[0]  # The first row contains the dates
stock_high = [float(value) for value in csv_list[1]]  # The second row contains the stock high values
stock_low = [float(value) for value in csv_list[2]]   # The third row contains the stock low values
stock_open = [float(value) for value in csv_list[3]]  # The fourth row contains the stock open values

# Plot the data
plt.style.use('ggplot')

plt.subplot(3, 1, 1)
plt.plot(date, stock_high, color='green', linestyle='dashed', marker='s', linewidth=3, label='Stock High')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Value')

plt.subplot(3, 1, 2)
plt.plot(date, stock_open, color='red', linestyle='-', marker='o', linewidth=2, label='Stock Open')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Value')

plt.subplot(3, 1, 3)
plt.plot(date, stock_low, color='yellow', linestyle='-', marker='v', linewidth=2, label='Stock Low')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Value')

plt.tight_layout()
plt.show()