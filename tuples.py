def tuple_product(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

# Example usage
given_tuple = (2, 3, 5, 7)
result = tuple_product(given_tuple)
print(f"The product of the numbers in the tuple {given_tuple} is {result}")
