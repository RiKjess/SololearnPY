"""
Regular expressions


You are playing a word game with your friends, and are asked for a word starting with "gl".
Write a program that takes the word as input and outputs "Match" if it starts with required characters, and "No match" if it doesn't.

Sample Input
glue

Sample Output
Match
"""

import re
pattern = r"gl"
word = input()
if re.match(pattern, word):
    print("Match")
else:
    print("No match")