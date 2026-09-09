marks = int(input("Enter Your Marks: "))

if marks > 90:
  print("Your Grade is A")
elif marks > 75 and marks <= 89:
  print("Your Grade is B")
elif marks > 50 and marks <= 74:
  print("Your Grade is C")
else:
  print("You are Fail")

