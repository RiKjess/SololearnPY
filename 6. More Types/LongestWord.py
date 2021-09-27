"""
Longest Word


Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome
"""

txt = input()
txt = txt.split()
print(max(txt, key=len))