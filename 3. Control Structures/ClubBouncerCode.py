"""
else Statement


Write a program to control entrance to a club.
Only people who are 18 or older are allowed to enter the club.
Your program takes the age and the name of the person who tries to enter, and outputs "Welcome" followed by the name of the person if they are allowed to enter the club, and "Sorry" if they are younger than the allowed age.

Sample Input
24
James

Sample Output
Welcome James
"""

age = int(input())
name = input()
if int(age) >= 18:
    print ("Welcome " + str(name))
else:
    print ("Sorry")