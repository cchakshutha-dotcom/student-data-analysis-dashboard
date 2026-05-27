import pandas as pd

data = pd.read_excel('student.xlsx')

print(data['marks'].mean())
print(data.info())
print(data['marks'].max())
print(data[data['marks']>80])
print(data.describe())
print(data.isnull())
print(data['marks'].median())
print(data['marks'].mode())
print(data['marks'].std())
print(data['marks'].value_counts())
print(data.isnull().sum())
print(data.dropna())
data['marks'] = data['marks'].fillna(data['marks'].mean())
print(data)
print(data.drop_duplicates())