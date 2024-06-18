import matplotlib.pyplot as plt

b_count = [115, 268, 319, 24, 199, 782, 500]
peeps = ["Conie", "Jackson", "Mathew", "Gavin", "Mumu", "Derek", "Bryann"]
twinks = [115, 200, 300, 1, 190, 360, 250]
twunks = [0, 68, 19, 23, 9, 422, 250]

line1 = plt.plot(peeps, b_count, color = "black", linestyle = "-.", marker = "o",
                 linewidth = 2, label = "Total")
line2 = plt.plot(peeps, twinks, color = "red", linestyle = "-.", marker = "o",
                 linewidth = 2, label = "PTO")
line3 = plt.plot(peeps, twunks, color = "blue", linestyle = "-.", marker = "o",
                 linewidth = 2, label = "Wellness Time")
plt.title("Vacation Hours Used")
plt.xlabel("Employee")
plt.ylabel("Hours")
plt.legend()
plt.show()
