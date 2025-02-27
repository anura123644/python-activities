import turtle # Importing library

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("orange")
screen.setup(300, 400)

# Create a turtle
polygon = turtle.Turtle() # Defined variable

# Variables for a square
num_side = 4  # Square has 4 sides
side_length = 70
angle = 360.0 / num_side

# Iterate loops for total number of sides
for i in range(num_side):
    polygon.forward(side_length)
    polygon.right(angle)

# Finish drawing
turtle.done()
