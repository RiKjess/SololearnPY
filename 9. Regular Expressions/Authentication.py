"""
More Metacharacters


Let's imagine we are creating our own authentication system.
Create a program that takes a password as input and returns "Password created" if
- it has at least one uppercase character
- it has at least one number

The Program should output "Wrong format" if requirements above are not met.

Sample Input
Hal44gb8

Sample Output
Password created
"""

import re
password = input()


pattern = r"[A-Z0-9]+"

if re.match(pattern, password):
    print("Password created")
else:
    print("Wrong format")