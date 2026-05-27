import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("student.xlsx")

print(df.columns)

# Fix column name
df["Result"] = df["marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

plt.figure(figsize=(10,8))

# Histogram
plt.subplot(2,2,1)
plt.hist(df["marks"])
plt.title("Marks Distribution")

# Pie
plt.subplot(2,2,2)
df["Result"].value_counts().plot(kind='pie', autopct='%1.1f%%')

# Box
plt.subplot(2,2,3)
plt.boxplot(df["marks"])

# Bar
plt.subplot(2,2,4)
df["marks"].plot(kind='bar')

plt.tight_layout()
plt.show()