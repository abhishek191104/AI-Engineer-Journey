import matplotlib.pyplot as plt

#1. Line Plot
days = [1, 2, 3, 4, 5]
sales = [100, 150, 130, 180, 220]

plt.plot(days, sales)

plt.title("Daily Sales")
plt.xlabel("Day")
plt.ylabel("Sales")

plt.show()

"""
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
visitors = [62, 33, 44, 38, 77, 90, 200]

plt.plot(week, visitors)

plt.title("Weekly Visitors")
plt.xlabel("Week")
plt.ylabel("Visitors")

plt.show()
"""
#2. Bar Chart
students = ["A", "B", "C", "D"]
Marks = [78, 92,65,88]

plt.bar(students, Marks)

plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()

'''
Subjects = ["Python", "SQL", "Math", "Java"]
Marks = [78, 92,65,88]

plt.bar(Subjects, Marks)

plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()
'''
#3.Scatter Plot
hours = [1, 2, 3, 4, 5, 6]
marks = [45, 50, 58, 65, 75, 85]

plt.scatter(hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()

#4.Pie chart
subjects = ["Python", "SQL", "Math"]
marks = [85, 80, 90]

plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%"
)

plt.title("Subject Distribution")

plt.show()

#5.Histogram
marks = [45, 50, 55, 60, 60, 65, 70, 72, 75, 80, 85, 90, 95]

plt.hist(marks)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()

#6.Multiple Lines + Legend
days = [1, 2, 3, 4, 5]

python_marks = [60, 65, 70, 80, 85]
sql_marks = [55, 68, 72, 78, 90]

plt.plot(days, python_marks, label="Python")
plt.plot(days, sql_marks, label="SQL")

plt.title("Performance")
plt.xlabel("Day")
plt.ylabel("Marks")

plt.legend()

plt.show()

#7.Subplots
plt.subplot(1, 2, 1)

plt.bar(["Python", "SQL", "Math"], [85, 80, 90])
plt.title("Marks")


plt.subplot(1, 2, 2)

plt.pie([85, 80, 90], labels=["Python", "SQL", "Math"])
plt.title("Distribution")

plt.show()