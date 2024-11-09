class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive .")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"


# Example usage
account1 = BankAccount("Alice", 500)
print(account1)
account1.deposit(200)
account1.withdraw(100)
print(f"Final balance: {account1.get_balance()}")
