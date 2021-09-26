"""
Boolean Logic


You need to create a program that outputs whether a store is Open or Closed, based on the hour and the day of the week.
The store is open on all days from 10 to 21, except Saturday and Sunday.
You need to take the hour and the day of the week as input.
The day of the week is represented as an integer (1 for Monday, 2 for Tuesday, etc.)

Sample Input:
15
4

Sample Output:
Open
"""

hour = int(input())
day = int(input())
if hour >= 10 and hour <=21 and day >= 1 and day <= 5: print ("Open")
else: print ("Closed")