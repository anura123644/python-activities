def is_power_of_eight(n):
    # Step 1: Check if n is positive
    if n <= 0:
        return False

    # Step 2: Keep dividing by 8 while divisible
    while n % 8 == 0:
        n //= 8

    # Step 3: If we end up with 1, it's a power of 8
    return n == 1

# Input from user
try:
    number = int(input("Enter a number: "))
    if is_power_of_eight(number):
        print(f"{number} is a power of 8.")
    else:
        print(f"{number} is NOT a power of 8.")
except ValueError:
    print("Invalid input. Please enter an integer.")

