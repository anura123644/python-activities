class Dog:
    # Class variable
    species = "Canis familiaris"
    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed
    def display_details(self):
        # Method to display details
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}\n")
# Create instances for two different breeds
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Bella", "German Shepherd")
# Display details of each dog
dog1.display_details()
dog2.display_details()