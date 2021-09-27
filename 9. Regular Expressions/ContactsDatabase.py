"""
Regular expressions


We need to create a number formatting system for a contacts database.
Create a program that will take the phone number as input, and if the number starts with "00", replace them with "+".
The number should be printed after formatting.

Sample Input
0014860098

Sample Output
+14860098
"""

import re


number = str(input())

pattern = r"00"
match = re.search(pattern, number)
if match and match.start() == 0:
    newnumber = re.sub(pattern, "+", number)
    print(newnumber)
else:
    print(number)