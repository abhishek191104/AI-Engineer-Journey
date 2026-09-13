import math

print(math.sqrt(20))
print(math.pi)

import random

number = random.randint(1, 10)

print(number)



try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")