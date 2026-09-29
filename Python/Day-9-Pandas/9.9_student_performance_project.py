import  pandas as pd

df = pd.read_csv("Day-9/student_project.csv")
print("\n---Student Data---")
print(df)

print("\nAverage Python Marks:", df["Python"].mean())
print("Highest SQL Marks:", df["SQL"].max())
print("Lowest Math Marks:", df["Math"].min())

print("\nStudents With Python > 85:")
print(df[df["Python"] > 85])

print("\nStudents With SQL >= 90:")
print(df[df["SQL"] >= 90])

print("\nSort Students by Math:")
print(df.sort_values("Math", ascending = False))

df["Total"] = df["Python"] + df["SQL"] + df["Math"]
print("\nTotal Marks:")
print(df)

df["Average"] = df["Total"] / 3
print("\nUpdated Data with Average Column:")
print(df)

top_student = df.loc[df["Total"].idxmax()]
print("\nTop Student:")
print(top_student)

top_students = df.loc[df["Average"] >= 85]
print("\nStudents With Average >= 85:")
print(top_students)

print("\nTotal Students:", df["Name"].count())

df.to_csv("Day-9/student_project.csv", index=False)

print("\nResult saved to student_performance_result.csv")