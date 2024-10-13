# polymorphism_demo.py

import math

# Base class Shape
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Overriding the area method to calculate rectangle's area
    def area(self):
        return self.length * self.width

# Derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Overriding the area method to calculate circle's area
    def area(self):
        return math.pi * self.radius ** 2
