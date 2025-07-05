def reverse_bits(n):
    # Find the number of bits in the binary representation of n
    num_bits = n.bit_length()
    
    reversed_num = 0
    for i in range(num_bits):
        # Extract the i-th bit from n
        bit = (n >> i) & 1
        # Set the bit at the reversed position
        reversed_num |= bit << (num_bits - 1 - i)
    
    return reversed_num

# Example usage
number = int(input("Enter a number: "))
reversed_number = reverse_bits(number)
print(f"Original number: {number}")
print(f"Reversed bits number: {reversed_number}")

