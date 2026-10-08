import pandas as pd

df = pd.read_csv("Day-9/students.csv")

print("Complete Data:")
print(df)

print("\nNames:")
print(df["Name"])

print("\nName and Python:")
print(df[["Name", "Python"]])

print("\nFirst row:")
print(df.iloc[0])

print("\nFirst two rows:")
print(df.iloc[0:2])

print("\nStudents with Python > 85:")
print(df[df["Python"] > 85])

print("\nStudents with Math >= 85")
print(df[df["Math"] >= 85])

print("\nStudents with SQL >= 90:")
print(df[df["SQL"] >= 90])

print("\nSorted by Python:")
print(df.sort_values("Python"))

print("\nSorted by Python - Highest to Lowest:")
print(df.sort_values("Python", ascending=False))

print("\nSorted by SQL - Highest to Lowest:")
print(df.sort_values("SQL", ascending=False))

print("\nAverage Python Marks:")
print(df["Python"].mean())

print("\nHighest Python Marks:")
print(df["Python"].max())

print("\nLowest Python Marks:")
print(df["Python"].min())

print("\nSum of Python Marks:")
print(df["Python"].sum())

print("\nCount of Python Marks:")
print(df["Python"].count())