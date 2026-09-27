import pandas as pd

data = {
  "Name": ["Rahul", "Anita", "John", "Priya", "Arun"],
  "Age": [21, 22 , 23 ,20, 21],
  "Python": [85, 79, 80, 95, 88],
  "Math": [78, 95, 70, 85, 88],
  "Science": [82, 90, 72, 91, 86]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nAverage Python Score:")
print(df["Python"].mean())

print("\nAverage Math Score:")
print(df["Math"].mean())

print("\nAverage Science Score:")
print(df["Science"].mean())

print("\nStudents with Python score above 85:")
print(df[df["Python"] > 85])