import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

total = [115, 268, 319, 24, 199, 782, 500]
employees = ["Conie", "Jackson", "Mathew", "Gavin", "Mumu", "Derek", "Bryann"]
pto = [115, 200, 300, 1, 190, 360, 250]
wellness = [0, 68, 19, 23, 9, 422, 250]

x = np.arange(len(employees))
# print (x)

style.use ('ggplot')
# # vertical bar chart
# plt.bar(employees, total, label = 'Total')
# plt.bar(employees, pto, label = 'PTO')
# plt.bar(employees, wellness, label = 'Wellness Hours')

#horizontal bar chart
plt.barh(employees, total, label = 'Total')
plt.barh(employees, pto, label = 'PTO')
plt.barh(employees, wellness, label = 'Wellness Hours')


plt.xlabel ('Hours')
plt.ylabel ("Employees")
# plt.xticks(x, employees)
plt.title ('Time Off Usage')
plt.legend()
plt.show()