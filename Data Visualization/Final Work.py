import matplotlib.pyplot as plt
from matplotlib import style

Number_of_students = [138, 205, 232, 78]
university = ['AU', 'GMU', 'ISU', 'VTU']
style.use ('ggplot')
line1 = plt.plot(university, Number_of_students, color ='red', linestyle='--', marker='o', linewidth=2, label = 'Students')
plt.title('Student Enrollment')
plt.xlabel('University')
plt.ylabel('Number of Students')
plt.legend()
plt.show()