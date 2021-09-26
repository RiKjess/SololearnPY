"""
Exception Handling


We need to create a program that allows users to create their own PIN codes for their bank cards. Each PIN code consists of digits. Complete the program so that when the user enters a character, the program stops and outputs "Please enter a number" and when the user enters only digits, the program outputs "PIN code is created".

Sample Input
44a5

Sample Output
Please enter a number
"""

try:
	pin = int(input())
	print("PIN code is created")
	

except ValueError:
	print("Please enter a number")