"""
Function Arguments


Given a function that takes 2 arguments and returns their sum.
But we get an error when we want to sum more than 2 numbers. Change the function and complete the code so that the function sums as many numbers as are input.
"""

def adder(x, y, *args):
    n = sum(args)
    print(x+y+n)

adder(2, 3)
adder(2, 3, 4)
adder(1, 2, 3, 4, 5)