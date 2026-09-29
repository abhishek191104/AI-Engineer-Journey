import pandas as pd

data = {
    "Department": ["CSE", "ECE", "CSE", "ECE", "CSE"],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("Data:")
print(df)

print("\nAverage marks by department:")
print(df.groupby("Department")["Marks"].mean())

print("\nHighest marks by department:")
print(df.groupby("Department")["Marks"].max())

print("\nTotal marks by department:")
print(df.groupby("Department")["Marks"].sum())