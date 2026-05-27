import matplotlib.pyplot as plt

# Data
names = ["Ram", "Sita", "Ravi"]
marks = [80, 90, 75]

# Create 2x2 layout
plt.figure(figsize=(10, 8))

# 1. Line Plot
plt.subplot(2, 2, 1)
plt.plot(names, marks)
plt.title("Line Plot")

# 2. Bar Chart
plt.subplot(2, 2, 2)
plt.bar(names, marks)
plt.title("Bar Chart")

# 3. Histogram
plt.subplot(2, 2, 3)
plt.hist(marks)
plt.title("Histogram")

# 4. Pie Chart
plt.subplot(2, 2, 4)
plt.pie(marks, labels=names, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.tight_layout()
plt.show()