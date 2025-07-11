class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner          
        self.balance = balance      

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # Add money
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount  # Subtract money
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Withdraw amount must be positive!")

    def get_balance(self):
        return self.balance

# Create account and perform operations
account = BankAccount("Alice", 100)
account.deposit(50)  
account.withdraw(70)  
print("Current balance:", account.get_balance())