class student:
  college = "Mind college"

  def __init__(self, name, age, course):
    self.name = name
    self.age = age
    self.course = course

student1 = student("Abhishek", 21, "ECE")
student2 = student("Rahul", 20, "CSE")

print("\nStudent1:", student1.name)
print(student1.age)
print(student1.course)
print(student1.college)

print("\nStudent2:", student2.name)
print(student2.age)
print(student2.course)
print(student2.college)