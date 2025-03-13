# Function to calculate power
def calculate_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Input from user
base = int(input("Enter the base number: "))
exponent = int(input("Enter the power (exponent): "))

# Calculate and display the result
result = calculate_power(base, exponent)
print(f"{base} to the power of {exponent} is: {result}")
