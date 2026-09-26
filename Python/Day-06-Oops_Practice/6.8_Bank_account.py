
class BanK_Account:

  def __init__(self,account_holder,balance):
    self.account_holder = account_holder
    self.balance = balance

  def display_balance(self):
    print("\nAccount Holder:", self.account_holder)
    print("Current Balance:",self.balance)
  
  def deposit(self,amount):
    if amount > 0:
     self.balance += amount
     print("Amount Deposited Successfully!")
     print("Amount Deposited =", amount)
    else:
      print("Enter Valid Amount.")

  def withdraw(self,amount):
    if amount <= 0:
      print("Enter Valid Amount.")
    elif amount > self.balance:
      print("Insufficient Balance.")
    else:
      self.balance -= amount
      print("Amount Withdrawn Successfully!")
      print("Withdrawn:",amount)
    
account = BanK_Account("Abhishek Chitturi",30000)

while True:
  print("\n=== Bank Account ===")
  print("1.Display Balance")
  print("2.Deposit Money")
  print("3.Withdraw Money")
  print("4.Exit")

  choice = input("Enter Choice: ")

  if choice == "1":
    account.display_balance()

  elif choice == "2":
    amount = float(input("Enter depost ammount: "))
    account.deposit(amount)

  elif choice == "3":
    amount = float(input("Enter Withdraw Amount: "))
    account.withdraw(amount)

  elif choice == "4":
    print("Thank You for using the Bank Account System.")
    break

  else:
    print("Enter Valid Input.")