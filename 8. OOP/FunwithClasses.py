"""
Inheritance


Complete the provided code to inherit the Car class from the Vehicle class, create a Car object and call its horn() method, which is inherited from the Vehicle superclass.
class Vehicle: 
  def horn(self):
    print("Beep!")

class Car:
  def __init__(self, name, color):
    self.name = name
    self.color = color

obj = Car("BMW", "red") 
"""

class Vehicle: 
    def __init__(self, name, color):
        self.name = name
        self.color = color    

    def horn(self):
        print("Beep!")

class Car(Vehicle):
    def horn(self):
        print("Beep!")

obj = Car("BMW", "red")
obj.horn()