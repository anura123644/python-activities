# Tasks using list comprehensions

nums = list(range(1, 11))  # Numbers from 1 to 10
words = ['python', 'list', 'comprehension', 'practice']
nested_list = [[1, 2], [3, 4], [5, 6]]

# 1. List of squares
squares = [x**2 for x in nums]

# 2. Extract even numbers
evens = [x for x in nums if x % 2 == 0]

# 3. Convert strings to uppercase
uppercase_words = [word.upper() for word in words]

# 4. Replace even/odd numbers with 'Even'/'Odd'
labels = ['Even' if x % 2 == 0 else 'Odd' for x in nums]

# 5. Flatten a nested list
flat_list = [item for sublist in nested_list for item in sublist]

# Print results
print("Squares:", squares)
print("Even numbers:", evens)
print("Uppercase words:", uppercase_words)
print("Even/Odd labels:", labels)
print("Flattened list:", flat_list)
