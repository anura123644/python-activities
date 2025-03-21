
test_dict = {'a': 3, 'b': 2, 'c': 3, 'd': 1, 'e': 3}

value_to_check = 3
frequency = 0

for val in test_dict.values():
    if val == value_to_check:
        frequency += 1

print(f"The frequency of value {value_to_check} is: {frequency}")
