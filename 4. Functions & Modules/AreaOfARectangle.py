"""
Arguments


We need to calculate the area of the rectangle.
Complete and call the function to output the area of the rectangle, taking 2 arguments as length and width. If sides are equal, the function should also show "Square" as the second output.

Sample Input 1
7
4

Sample Output 1
28
"""

length = int(input())
width = int(input())
def area(length, width):
	if length == width:
		print(length * width)
		print("Square")
	else:
		print(length * width)

area(length, width)