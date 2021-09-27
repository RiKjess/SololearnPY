"""
Word Counter


Given text as input, output the number of words it contains.

Sample Input
hello world

Sample Output
2
"""

txt = input()

txt=txt.split()
print(len(txt))