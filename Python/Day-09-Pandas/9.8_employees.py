import pandas as pd

df = pd.read_csv("Day-9/employees.csv")

print("\nData:")
print(df)

print("\nAverage salary by department:")
print(df.groupby("Department")["Salary"].mean())

print("\nMaximum salary by department:")
print(df.groupby("Department")["Salary"].min())

print("\nTotal salary by department:")
print(df.groupby("Department")["Salary"].sum())