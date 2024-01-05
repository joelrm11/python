class BankAccount:
    interest_rate = 0.03  # Class variable for interest rate

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")
            
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
            
    def display_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance}")
        
# Create instances of BankAccount
account1 = BankAccount("A12345", 1000)
account2 = BankAccount("B67890", 2000)

# Display initial balances
account1.display_balance()
account2.display_balance()

# Deposit and withdraw from accounts
account1.deposit(500)
account2.withdraw(300)

# Display updated balances
account1.display_balance()
account2.display_balance()

# Access class variable (interest rate) through an instance
print("Interest Rate:", account1.interest_rate)
print("Interest Rate:", account2.interest_rate)

# Access class variable (interest rate) through the class
print("Class Interest Rate:", BankAccount.interest_rate)
