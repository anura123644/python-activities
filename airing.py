def find_rightmost_set_bit(n):
    if n == 0:
        return "No set bits in 0."
    
    # Isolate the rightmost set bit
    rightmost_set_bit = n & -n

    # Find the position (1-based index)
    position = 1
    while rightmost_set_bit > 1:
        rightmost_set_bit >>= 1
        position += 1

    return f"Rightmost set bit is at position: {position}"

# Input from user
try:
    number = int(input("Enter a number: "))
    result = find_rightmost_set_bit(number)
    print(result)
except ValueError:
    print("Please enter a valid integer.")

