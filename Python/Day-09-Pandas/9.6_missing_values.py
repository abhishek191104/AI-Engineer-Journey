import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [85, None, 90, 78]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nMissing values:")
print(df.isnull())

print("\nNumber of missing values:")
print(df.isnull().sum())

print("\nAfter removing missing values:")
print(df.dropna())

df["Marks"] = df["Marks"].fillna(0)

print("\nAfter filling missing values with 0:")
print(df)