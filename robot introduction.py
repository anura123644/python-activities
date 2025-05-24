class Robot:
    def __init__(self, name, birth_year, activity):
        self.name, self.birth_year, self.activity = name, birth_year, activity

    def introduce(self):
        return f"Hello! I am {self.name}, born in {self.birth_year}, and I love {self.activity}."

my_robot = Robot("Anurag", 2014, "coding")
print(my_robot.introduce())

