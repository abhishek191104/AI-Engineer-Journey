class person:

  def __init__(self,name):
    self.name = name

  def display_name(self):
    print("Name:",self.name)

class Employee(person):

  def __init__(self,name,salary):
    super().__init__(name)
    self.salary = salary

  def display_salary(self):
    print("Salary:",self.salary)

employee1 = Employee("Abhishek", 20000)

employee1.display_name()
employee1.display_salary()
