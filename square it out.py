# Input the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Create a list of square values
squares = [num**2 for num in range(start, end + 1)]

# Separate odd and even values
odd_squares = [num for num in squares if num % 2 != 0]
even_squares = [num for num in squares if num % 2 == 0]

# Output the results
print("Squares:", squares)
print("Odd Squares:", odd_squares)
print("Even Squares:", even_squares)
