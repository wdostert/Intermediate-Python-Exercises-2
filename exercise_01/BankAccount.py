class BankAccount:
    def __init__(self, account_name, starting_balance):
        self.name = account_name
        self.balance = starting_balance


    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return f"{self.name} has a balance of ${self.balance}."