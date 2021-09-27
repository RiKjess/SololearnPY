"""
Tuples


You are given coordinates of 2 points and need to find the straight line distance between them.

The coordinates are provided in a tuple, for example:
p = (8, 11) 
PY
The first value represents the x coordinate, while the second value represents the y coordinate of the point p.

Complete the provided code to calculate and output the distance between the two given points.
"""

import math

p1 = (23, -88)
p2 = (6, 42)

a=p2[0]-p1[0]
b=p2[1]-p1[1]

c=math.sqrt(a**2+b**2)
print(c)