"""
Decorators


You are working on a restaurant software, which has a function to print the bill.

You need to add a decorator, which adds 3 hashtags before and after the bill data, so that the start and end of the printed bill can be identified.

Add a decorator to the code that adds ### before and after the print_bill() method.
"""

def decor(func):
    def wrap():
        print("###")
        func()
        print("###")
    return wrap


def print_bill():
    print("BILL DATA GOES HERE")

decoration = decor(print_bill)
decoration()