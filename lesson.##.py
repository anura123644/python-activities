# Program to count the total number of digits in a number

# Taking input from the user
number = int(input("Enter a number: "))

# Initializing the digit count to 0
count = 0

# Using a while loop to count the digits
while number != 0:
    number = number // 10
    count += 1

# Displaying the total number of digits
print(f"The total number of digits is: {count}")
