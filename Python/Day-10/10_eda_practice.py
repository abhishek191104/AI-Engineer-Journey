import pandas as pd

# Read CSV file
df = pd.read_csv("Day-10/10.4_student_data.csv")

print("===== FIRST FIVE ROWS =====")
print(df.head())


print("\n===== DATASET SHAPE =====")
print(df.shape)


print("\n===== DATASET INFORMATION =====")
df.info()


print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())


print("\n===== MISSING VALUES =====")
print(df.isnull().sum())


print("\n===== AVERAGE MARKS =====")
print(df["Marks"].mean())


print("\n===== HIGHEST MARKS =====")
print(df["Marks"].max())


print("\n===== LOWEST MARKS =====")
print(df["Marks"].min())


print("\n===== STUDENT WITH HIGHEST MARKS =====")

highest_student = df.loc[df["Marks"].idxmax()]

print(highest_student)


print("\n===== STUDENT WITH LOWEST MARKS =====")

lowest_student = df.loc[df["Marks"].idxmin()]

print(lowest_student)


print("\n===== AVERAGE STUDY HOURS =====")
print(df["Hours_Studied"].mean())


print("\n===== AVERAGE ATTENDANCE =====")
print(df["Attendance"].mean())