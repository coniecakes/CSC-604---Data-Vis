import matplotlib.pyplot as plt

b_count = [115, 268, 319, 24, 199, 782, 500]
peeps = ["Conie", "Jackson", "Mathew", "Gavin", "Mumu", "Derek", "Bryann"]
twinks = [115, 200, 300, 1, 190, 360, 250]
twunks = [0, 68, 19, 23, 9, 422, 250]

line1 = plt.plot(peeps, b_count, color = "pink", linestyle = "-.", marker = "*",
                 linewidth = 2, label = "Total")
line2 = plt.plot(peeps, twinks, color = "red", linestyle = "--", marker = "*",
                 linewidth = 2, mec = "blue", label = "Twinks")
line3 = plt.plot(peeps, twunks, color = "black", linestyle = "-", marker = "*",
                 linewidth = 2, mec = "pink", label = "Twunks")
plt.title("Body Count")
plt.xlabel("My Friends")
plt.ylabel("Bois Destoryed")
plt.legend()
plt.show()
