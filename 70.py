# Parent class
class Vehicle:
    def __init__(self, name, seats):
        self.name = name
        self.seats = seats

    def fare(self):
        return self.seats * 100  # Default fare per seat is 100

# Child class
class Bus(Vehicle):
    def __init__(self, name, seats):
        super().__init__(name, seats)

    # Overriding the fare method
    def fare(self):
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.1  # 10% extra for maintenance
        return base_fare + maintenance_charge

# Example usage
school_bus = Bus("School Bus", 50)
print(f"The total fare for the {school_bus.name} is: ₹{school_bus.fare()}")
