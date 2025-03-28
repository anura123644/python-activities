from abc import ABC, abstractmethod

# Abstract base class
class Car(ABC):
    @abstractmethod
    def brand_name(self):
        pass

    @abstractmethod
    def top_speed(self):
        pass

# BMW class implementing the abstract methods
class BMW(Car):
    def brand_name(self):
        return "BMW"

    def top_speed(self):
        return "Top speed: 250 km/h"

# Ferrari class implementing the abstract methods
class Ferrari(Car):
    def brand_name(self):
        return "Ferrari"

    def top_speed(self):
        return "Top speed: 340 km/h"

# Function demonstrating polymorphism
def display_car_details(car):
    print(f"Brand: {car.brand_name()}")
    print(f"{car.top_speed()}")

# Creating objects of BMW and Ferrari
car1 = BMW()
car2 = Ferrari()

# Using polymorphism
display_car_details(car1)
display_car_details(car2)