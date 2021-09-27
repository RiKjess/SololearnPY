import re

number = input("Enter your phone number: ")

def new_func(number):
    pattent = r"^(1|8|9)\d{7}$"

    if re.match(pattent, number):
        print("Valid")
    else:
        print("Invalid")

new_func(number)
