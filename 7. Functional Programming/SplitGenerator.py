"""
Generators


Given a string as input, create a generator function that splits the string into separate words and outputs the resulting list.

Sample Input
This is some text

Sample Output
['This', 'is', 'some', 'text']
"""

txt = input()

def words():
    
    for i in txt.split():
        yield i

print(list(words()))