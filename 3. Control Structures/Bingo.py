"""
List Operations


Given a list of numbers, output "bingo" if it contains the input number.
"""

items = [42, 88, 721, 12, 43, 22, 908]

num = int(input())
if num in items:
    print("bingo")