import pandas as pd

data = {
  "Name": ["Abhishek", "Rahul", "Priya", "Anjali"],
  "Age": [22, 21, 23, 22],
  "Marks": [85, 90, 78, 92]
}
df = pd.DataFrame(data)
print(df)

print("\nFirst rows:")
print(df.head())

print("\nLast rows:")
print(df.tail())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nInformation:")
df.info()

print("\nStatistics:")
print(df.describe())

#Practice
data1 = {
  "Name": ["Arun", "Ravi", "Priya", "Sneha"],
  "Age": [21, 22, 20, 21],
  "Marks": [85, 92, 78, 95]
}
df = pd.DataFrame(data1)
print(df)