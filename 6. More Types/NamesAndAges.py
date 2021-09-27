"""
String Formatting


The .format() method provides an easy way to format strings.
Take as input a name and an age, and generate the output "name is age years old".

Sample Input
James
42

Sample Output
James is 42 years old
"""

name = input()
age = int(input())


msg = "{y} is {x} years old".format(y=name, x=age)
print(msg)