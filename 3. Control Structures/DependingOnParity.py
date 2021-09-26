"""
elif Statements


Write a program that takes a number as input and
- returns its double, if the number is even
- returns its triple, if the number is odd
- returns 0, if number is 0

Sample Input:
1

Sample Output:
3
"""

number = input()
if (int(number) % 2 == 0):
    print (int(number) * 2)
elif (int(number) % 2 != 0):
    print (int(number) * 3)    
elif (int(number) == 0):
    print (0)