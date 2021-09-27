"""
else and Exception Handling


To order a restaurant dish online, the user should enter the code of desired dish, which contains only digits. Write a program that will take the code as input, and output "Enter only digits" if it contains non-digit symbols, and output "Order accepted" if it doesn't.
If the ordering process went well, the program also should output "Bon appetit".

Sample Input
1437

Sample Output
Order accepted
Bon appetit
"""

code = input()

try:
    if code.isdigit():
        print("Order accepted")
    else:
        raise ValueError	
except ValueError:
    print("Enter only digits")
else:
	print("Bon appetit")