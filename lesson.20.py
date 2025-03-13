import math

# Function to calculate the square root
def calculate_square_root(number):
    if number < 0:
        return "Square root of negative numbers is not defined in real numbers."
    return math.sqrt(number)

# Input from the user
number = float(input("Enter a number to find its square root: "))

# Calculate and display the square root
result = calculate_square_root(number)
print(f"The square root of {number} is {result}")
