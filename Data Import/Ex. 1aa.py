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
    stock_data_list = list(csvdata)

# Transpose the data to read it correctly
transposed_data = list(zip(*stock_data_list))

# Extract the data
date = transposed_data[0]
stock_high = [float(value) for value in transposed_data[1]]
stock_open = [float(value) for value in transposed_data[2]]
stock_low = [float(value) for value in transposed_data[3]]

# Create a 3x2 grid of plots
fig, axs = plt.subplots(3, 2, figsize=(15, 10))

# Plot stock high values
axs[0, 0].plot(date, stock_high, label='High')
axs[0, 0].set_title('Stock High')
axs[0, 0].legend()

# Plot stock open values
axs[0, 1].plot(date, stock_open, label='Open')
axs[0, 1].set_title('Stock Open')
axs[0, 1].legend()

# Plot stock low values
axs[1, 0].plot(date, stock_low, label='Low')
axs[1, 0].set_title('Stock Low')
axs[1, 0].legend()

# Leave the other boxes empty
axs[1, 1].axis('off')
axs[2, 0].axis('off')
axs[2, 1].axis('off')

# Adjust layout and show plot
plt.tight_layout()
plt.show()