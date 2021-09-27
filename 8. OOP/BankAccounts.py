"""
Operator Overloading


The __add__ method allows for the definition of a custom behavior for the + operator in our class.

The provided code is trying to add together two BankAccount objects, which should result in a new object with the sum of the balances of the given accounts.
Fix the code to make it work as expected and output the resulting account balance.
"""

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return BankAccount(self.balance + other.balance)

a = BankAccount(1024)
b = BankAccount(42)

result = a + b
print(result.balance)