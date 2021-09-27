"""
Classes


Given a Rectangle class, create a program to take two integer numbers as input, assign them as the width and height of a Rectangle object and output the volume of the resulting rectangle.
class Rectangle:
def __init__(self, width, height):
     self.w = width
      self.h = height  
Sample Input
5
4

Sample Output
20
"""

class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height
    def vol(self):
       return (w*h)
       
        
w = int(input())
h = int(input())

obj = Rectangle(w, h)
print(obj.vol())