#practice-1 print function
def hello(name):
   print("Hello!", name)
hello("Abhishek")

#practice-2 square of a number 
def square(n):
   return(n**2)
print(f"Square of your Number: ", square(5))

#practice-3 is_even
def is_even(n):
   return(n % 2 == 0)
print(f"Your Number is Even: ", is_even(100))

#practice-4 Largesr Number
def larger_number(a, b):
    if a > b:
        return a
    else:
        return b
print(larger_number(20,30))

"""def larger_number(a, b):
    return max(a, b)"""

#practice-5 name and age
def profile(name,age):
    print(f"My Name is {name} and I am {age} years old.")
profile("Abhishek",21)

#practice-6 Area of Rectangle
def area_rectangle(len, width):
    return(len * width)
print(f"Area of rectangle:",area_rectangle(10,8) )    

#practice-7 accepts a list and returns the sum of all numbers
def calculate_sum(*n):
    return(sum(n)) 
print(f"Sum of Numbers is: ", calculate_sum(11,22,33,44,55,66))

#practice-8  Create a function that counts how many even numbers are present in a list.
def count_even(*n):
    return sum(1 for num in n if num % 2 == 0)
print(f"Total Even Numbers are: ", count_even(1,2,3,4,5,6,7,8,8,8,3,2))

