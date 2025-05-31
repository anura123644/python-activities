from abc import ABC, abstractmethod

# Abstract class
class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

# Derived class for Rectangle
class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Derived class for Triangle
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Derived class for Circle
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.1416 * (self.radius ** 2)

# Example usage
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 6)
circle = Circle(7)

print("Rectangle Area:", rectangle.area())
print("Triangle Area:", triangle.area())
print("Circle Area:", circle.area())

