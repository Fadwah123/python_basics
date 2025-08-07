class BankAccount:
    def __init__ (self,balance=0):
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"Depositing ₹{amount}...")
        self.check_balance()

    def withdraw(self,amount):
        if amount>self.balance:
            print(f"Withdrawing ₹{amount}...")
            print("❌ Error: Insufficient funds")
        else:
            print(f"Withdrawing ₹{amount}...")
            self.check_balance()

    def check_balance(self):
        print(f"Balance:₹{self.balance}")
            

print("Welcome to Python Bank!")
acc1=BankAccount(5000)
acc1.check_balance()
acc1.deposit(1000)
acc1.withdraw(7000)
