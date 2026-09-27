#1.Create a Series
import pandas as pd
numbers = pd.Series([10, 20, 30, 40, 50])
print(numbers)

#2.Create a DataFrame
data = {
  "Name": ["Abhishek", "Rahul", "Tina"],
  "Age": [21, 30, 23],
  "Score": [85, 79, 89]
}

df = pd.DataFrame(data)
print(df)

#3.Select columns
print(df["Name"])
print(df["Score"])

#4.Select rows
print(df.iloc[0])
print(df.iloc[1])
print(df.iloc[2])

#4.Basic DataFrame information
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

#5.Filtering Data
import pandas as pd

data = {
    "Name": ["Rahul", "Anita", "John", "Priya"],
    "Age": [21, 22, 20, 23],
    "Score": [85, 90, 78, 95]
}

df = pd.DataFrame(data)

print(df[df["Score"] > 85])