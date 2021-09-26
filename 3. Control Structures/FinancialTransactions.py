"""
Chaining Multiple Conditions


Using an ATM, customers can access their bank deposits or credit accounts to do a variety of financial transactions.
You serve ATMs that accept only Visa and Amex bank cards.
The given program takes the type of a bank card as input.

Task
Complete the program to output "accepted" if the card is Visa or Amex.
Don't output anything otherwise.

Sample Input
Amex

Sample Output
accepted
"""

type = input()

if type == "Visa" or type == "Amex":
    print("accepted")