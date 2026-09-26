class student:
  print("\nStudent Details: ")

  def __init__(self, name, roll_no, marks):
    self.name = name
    self.roll_no = roll_no
    self.marks = marks

  def display(self):
    print("\nName: ", self.name)
    print("Roll Number: ", self.roll_no)
    print("Marks: ", self.marks)

  def calculate_grade(self):
      if self.marks >= 90:
        print("Grade: A")
      elif self.marks >= 80:
        print("Grade: B")
      elif self.marks >= 70:
        print("Grade: C")
      elif self.marks >= 60:
        print("Grade: D")
      else:
        print("Grade: F")

student1 = student("Abhishek", 201, 85)
student2 = student("Rahul", 202, 95)

student1.display()
student1.calculate_grade()
student2.display()
student2.calculate_grade()
