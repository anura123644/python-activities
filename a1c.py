from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.__width = width  # Encapsulated attribute
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height

class Triangle(Polygon):
    def __init__(self, base, height):
        self.__base = base
        self.__height = height

    def calculate_area(self):
        return 0.5 * self.__base * self.__height

# Example usage
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 6)

print("Rectangle Area:", rectangle.calculate_area())
print("Triangle Area:", triangle.calculate_area())

