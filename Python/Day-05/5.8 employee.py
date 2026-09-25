class Employee:

   def __init__(self, name, salary, department):
      self.name = name
      self.salary = salary 
      self.department = department

   def display_details(self):
      print("\nName:",self.name)
      print("Salary:",self.salary)
      print("Department:",self.department)
employee1 = Employee("Venkat", 25000, "HR Department")
employee2 = Employee("Raju", 12000, "Production")

print("\n___Employee Details___")

employee1.display_details()
employee2.display_details()
