"""
Static Methods


Complete the given code to define a static add() method for the Calculator class, which returns the sum of its parameters.

The code takes two numbers as input, and should return their sum using the Calculator class's add() method.
"""

class Calculator:
    @staticmethod
    def add(n1, n2):
        return n1+n2
        
n1 = int(input())
n2 = int(input())

print(Calculator.add(n1, n2))