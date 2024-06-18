import matplotlib.pyplot as plt

total = [115, 268, 319, 24, 199, 782, 500]
employees = ["Conie", "Jackson", "Mathew", "Gavin", "Mumu", "Derek", "Bryann"]
pto = [115, 200, 300, 1, 190, 360, 250]
wellness = [0, 68, 19, 23, 9, 422, 250]
days = [100, 85, 24, 500, 320, 10, 150]


plt.subplot(3,2,1)
line1 = plt.plot(employees, total, color = "black", linestyle = "-.", marker = "o",
                 linewidth = 2, label = "Total")
# plt.title("Vacation Hours Used")
# plt.xlabel("Employee")
# plt.ylabel("Hours")
plt.legend()

plt.subplot(3,2,2)
line2 = plt.plot(employees, pto, color = "red", linestyle = "-.", marker = "o",
                 linewidth = 2, label = "PTO")
# plt.title("Vacation Hours Used")
# plt.xlabel("Employee")
# plt.ylabel("Hours")
plt.legend()

plt.subplot(3,2,3)
line3 = plt.plot(employees, wellness, color = "blue", linestyle = "-.", marker = "o",
                 linewidth = 2, label = "Wellness Time")
# plt.title("Vacation Hours Used")
# plt.xlabel("Employee")
# plt.ylabel("Hours")
plt.legend()

plt.subplot(3,2,4)
line4 = plt.plot(employees, days, color = "green", linestyle = "-.", marker = "o",
                 linewidth = 2, label = "Remaining Time")
plt.legend()
plt.subplot(3,2,5)
line5 = plt.plot(employees, days, color = "orange", linestyle = "-.", marker = "o",
                 linewidth = 2, label = "Data Set 5")
plt.subplot(3,2,6)
line6 = plt.plot(employees, days, color = "pink", linestyle = "-.", marker = "o",
                 linewidth = 2, label = "Data Set 6")
plt.show()
