"""
List Comprehensions


Write a program to take a number as input, and output a list of all the numbers below that number, that are a multiple of both, 3 and 5.

Sample Input
42

Sample Output
[0, 15, 30]
"""

x = int(input()) 

out = [i for i in range(x) if i%3==0 and i%5==0 and i<x]

print(out)