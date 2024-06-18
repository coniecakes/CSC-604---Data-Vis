import matplotlib.pyplot as plt
from matplotlib import style
import csv
# import the csv module to help us read csv files easily
# csv = comma separarted values

num_students = []
num_women = []
num_men = []
majors = []

# open the csv
file_handle = open('intro_to_python.txt','r') # using a built-in python command to open file in 'read' mode
#read from the csv file
csvdata = csv.reader(file_handle) #read the data and save in a variable called csvdata

# #convert the data into a list of lists
csv_list = list(csvdata)
#print (csv_list) #uncomment to see how the list looks

#print (csv_list[2][0])
# #get data fom the csv lists and put them into our data lists

for elem in csv_list:
    print (elem)
    majors.append(elem[0])
    num_students.append(int(elem[1]))
    num_women.append(int(elem[2]))
    num_men.append(int(elem[3]))

file_handle.close() #very important to close the file handle after you have worked with the file
#
print (majors)
print (num_students)
# #
# # #
# #now use matplotlib to chart the lists
style.use ('ggplot')
# #print (style.available)
#
fig1 = plt.figure(1)

# #create a subplot comprising of 3 rows, 1 column and this is the first subplot
plt.subplot(3,1,1)
line1 = plt.plot(majors, num_students,
                 color = 'green',
                 linestyle = 'dashed',
                 marker = 's',
                 linewidth = 3,
                 label = 'Total'
                 )
plt.legend()
plt.xlabel ('Majors')
plt.ylabel ("Number of students")
plt.title ('Majors vs Number of students')

#create a subplot comprising of 3 rows, 1 column and this is the second subplot
plt.subplot(312)
line2 = plt.plot(majors, num_women,
                 color = 'red',
                 linestyle = '-',
                 marker = 'o',
                 linewidth = 2,
                 label = 'Women'
                 )

plt.xlabel ('Majors')
plt.ylabel ("Female students")
#plt.title ('Majors vs Number of women')
plt.legend()

#create a subplot comprising of 3 rows, 1 column and this is the third subplot
plt.subplot(3,1,3)
line1 = plt.plot(majors, num_men,
                 color = 'yellow',
                 linestyle = '-',
                 marker = 'v',
                 linewidth = 2,
                 label = 'Men'
                 )
plt.legend()
plt.xlabel ('Majors')
plt.ylabel ("Male students")

plt.show()