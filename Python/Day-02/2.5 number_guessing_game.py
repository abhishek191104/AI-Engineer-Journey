secrete_number = 7

guess = int(input("Enter Your Guess: "))

while guess != secrete_number:
   guess = int(input("Guess the Number: "))

   if guess < secrete_number:
     print("Try Higher")
   elif guess > secrete_number:
     print("Try Lower")
   else:
     print("Congragulations! You Guessed correctly")
  