import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

num_students = [38, 25, 32, 7]
num_women = [18, 18, 10, 5]
num_men = [20, 7, 22, 2]
majors = ['CS', 'Mathematics', 'Engineering', 'Literature']

x = np.arange(len(majors))
print (x)

style.use ('ggplot')

plt.bar(x, num_students, label = 'total')
plt.bar(x, num_men, label = 'men')
plt.bar(x, num_women, label = 'women')
#
# #horizontal bar chart
# plt.barh(x, num_students, label = 'total')
# plt.barh(x, num_women, label = 'women')
#
#
# plt.xlabel ('Majors')
# plt.ylabel ("Number of students")
# plt.xticks(x, majors)
# plt.title ('Majors vs Number of students')
# plt.legend()
plt.show()