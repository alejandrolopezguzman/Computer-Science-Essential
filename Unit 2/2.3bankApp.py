
#1st National Bank of Browntown Online Banking Application


class Customer():
    #This is an OBJECT. It has properties of Withdraw, Deposit, BalanceCheck
    def __init__ (self, name, balance = 100.00):
        self.name = name
        self.balance = balance
        print("Account made for", name, " Current Balance: $", balance)
        

    def withdraw(self,amount,):
        self.balance = self.balance - amount
        return self.balance
    
    def deposit(self,amount):
    #Add the ability to deposit
        self.balance = self.balance + amount
        return self.balance

    #Add the ability to check balance


print("Welcome to the 1st National Bank of Browntown App")
print("All new customers get $100 deposited into their account for signing up!")
print()
name = input("Let's Get Started! What is your name: ")
customer = Customer(name)

while(True):
    print("What would you like to do: (1) Withdraw   (2) Deposit   (3) Check Balance   (4) Finish")
    choice = input("->")

    #Withdraws a amount of money set by the user from the current balance
    if choice == "1":
        print("How much are you withdrawing")
        amount = float(input("->"))
        customer.withdraw(amount)
        print("You have withdrawn ", amount)
        print("You have", customer.balance, "dollars")

    #Deposits a amount of money set by the user into the current balance
    if choice == "2":
        print("How much are you depositing?")
        amount = float(input("->"))
        customer.deposit(amount)
        print("You have deposited ", amount)
        print("You have", customer.balance, "dollars")

    #Shows current balance
    if choice == "3":
        print("You have", customer.balance, "dollars")


    #Stops the loop and program
    if choice == "4":
        print("Thank's for using the 1st National Bank of Browntown App")
        break
    
