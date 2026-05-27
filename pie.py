import matplotlib.pyplot as plt

names = ["Ram", "Sita", "Ravi"]
marks = [80, 90, 75]

plt.pie(marks, labels=names)

plt.savefig("piechart.png")   # 👈 THIS LINE