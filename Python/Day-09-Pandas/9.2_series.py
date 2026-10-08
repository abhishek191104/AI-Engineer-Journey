import pandas as pd
#1
marks = pd.Series(
  [80, 75, 90, 95, 77],
)
print("Marks:")
print(marks)

print("\nFirst Mark:", marks[0])

print("\nFoUrth Mark:", marks[3])

#2
subjects = pd.Series(
  [90, 85, 88],
  index = ["Python", "SQL", "Math"]
  )
print(subjects)

#3
course = pd.Series(
  [90, 85, 88, 93],
  index = ["Python", "SQL", "NumPy", "Pandas"]
)
print(course)
print("\nPandas Marks:", course["Pandas"])
