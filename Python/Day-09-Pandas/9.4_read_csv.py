import pandas as pd

df = pd.read_csv("Day-9/students.csv")
print(df)

print("\nFirst 2 Rows:")
print(df.head(2))

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

#1. select column
print(df["Name"])

#2. select Multiple Columns
print(df[["Name", "Python", "SQL"]])

#3. select the first row
print(df.iloc[0])

#4. select the first two rows
print(df.iloc[0:2])