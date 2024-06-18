import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

num_students = [38, 25, 32, 7]
num_women = [18, 18, 10, 5]
num_men = [20, 7, 22, 2]
majors = ['CS', 'Mathematics', 'Engineering', 'Literature']

x = np.arange(len(majors))

style.use ('ggplot')
#by default matplotlib.pyplot has a width of 0.8
width = .25
#yerr = (38 25 32 7)
plt.bar(x, num_students, width,  label = 'total' )

for i in x:
    plt.annotate( str(num_students[i]) ,  (x[i],num_students[i]) )


plt.bar(x+.25, num_men, width, label = 'men')
plt.bar(x+.5, num_women, width, label = 'women')

plt.xlabel ('Majors')
plt.ylabel ("Number of students")
plt.xticks(x+.25, majors)
plt.title ('Majors vs Number of students')
plt.legend()
plt.show()