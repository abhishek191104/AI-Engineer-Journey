student = {
    "name": "Abhishek",
    "age": 22,
    "subjects": ["Python", "SQL", "Math"],
    "marks": {
        "python": 85,
        "sql": 80,
        "math": 75
    }
}

print("Name:", student["name"])

print("Age:", student["age"])

print("Subjects:", student["subjects"])

print("Python Marks:", student["marks"]["python"])

print("All Marks:", student["marks"])

all_marks = student["marks"].values()
total_marks = sum(all_marks)
print("Total Marks:", total_marks)

average_marks = total_marks / len(all_marks)
print("Average Marks:", average_marks)

highest_mark = max(all_marks)
print("Highest Mark:", highest_mark)