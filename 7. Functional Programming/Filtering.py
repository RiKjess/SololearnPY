"""
filter


Given a list of names, output a list that contains only the names that consist of more than 5 characters.
"""

names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]

res = list(filter(lambda x: len(x)>5, names))
print(res)