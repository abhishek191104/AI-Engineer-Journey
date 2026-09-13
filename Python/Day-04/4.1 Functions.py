def greet(name):

  print("Hello", name)
greet("Abhishek")
greet("Rahul")

def welcome():
  print("Welcome to AI Engineering!")

welcome()


def add(a,b):
  print(a+b)
add(3,4)


def calcus(a,b):
  print(f"Numbers are: {a,b}")
  print(f" ADD: {a+b},\n SUB: {a-b},\n MULTIPLY: {a*b},\n DIVISION: {a/b}")
calcus(3,6)


def num(a,b):
  print(f"\n Numbers are: {a,b}")
  return (a+b, a-b, a*b, a/b)
result = num(10,20)
print(result)

def square(number):
  return number ** 2
result = square(6)
print(f"\n {result}")

def hello(name="User"):
    print("Hello", name)
hello("Abhishek")


def student(name, age):
    print(name, age)

student(age=22, name="Abhishek")

def add_numbers(*numbers):
   return sum(numbers)
print(add_numbers(10,20,30))
print(add_numbers(10,20,30,40,50))

def student_info(**info):
   print(info)

student_info(
   name = "Abhishek",
   age = "22",
   course = "B.Tech- ECE"
)


x = 10

def test():
    print(x)

test()

