"""
if Statements


You have been asked to coordinate the dance school competition․
The terms of the competition are as follows:
- if the score is 80 or more the participant gets a certificate
- if the score is 90 or more the participant gets a certificate and also is admitted to the school.
The given program takes the score as input.

Task
Complete the program that will output "certificate" if the score is greater than or equal to 80. On top of that, the program should also output "admitted" if the score is greater than or equal to 90.

Sample Input
91

Sample Output
certificate
admitted

Hint
Use nested if statements to handle all the conditions.
"""

score = int(input())

if score >= 80:
    print("certificate")
    if score >= 90:
        print("admitted")