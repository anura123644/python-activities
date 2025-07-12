def longest_ones(n):
    # Convert the number to its binary representation without the '0b' prefix
    binary_str = bin(n)[2:]

    # Split the string by '0' and find the length of the longest '1' sequence
    longest = max(map(len, binary_str.split('0')))

    return longest

# Example usage
number = int(input("Enter a number: "))
result = longest_ones(number)
print(f"Longest consecutive 1's in binary of {number}: {result}")

