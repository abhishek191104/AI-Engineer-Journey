class person:

  def __init__(self, name, age, city):
    self.name = name
    self.age = age
    self.city = city
person1 = person("Rohit", 25, "Hyderabad")

print(person1.name)
print(person1.age)
print(person1.city)

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("\nMy name is", self.name)
        print("My age is", self.age)


student = Student("Abhishek", 21)

student.introduce()
