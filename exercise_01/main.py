from BankAccount import BankAccount

will_account = BankAccount("Will", 143.56)
will_account.deposit(50.22)
will_account.withdraw(20.89)
print(will_account.get_balance())