class student:

  def __init__(self, name, age, course):
    self.name = name
    self.age = age
    self.course = course

  def display_details(self):
    print("\nName:",student1.name)
    print("Age:",student1.age)
    print("Course:",student1.course)

student1 = student("Abhishek", 21, "ECE")

print("\nStudent Details:")
student1.display_details()