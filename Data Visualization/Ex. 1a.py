import matplotlib.pyplot as plt

b_count = [115, 268, 319, 24, 199, 782, 500]
peeps = ["Conie", "Jackson", "Mathew", "Gavin", "Mumu", "Derek", "Bryann"]


line1 = plt.plot(peeps, b_count, color = "blue", linestyle = "-.", marker = "*",
                 linewidth = 2, mec = "red")


plt.title("Vacation Hours Used")
plt.xlabel("My Friends")
plt.ylabel("Hours")
plt.show()
plt.plot