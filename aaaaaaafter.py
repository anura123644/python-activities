def all_substrings(s):
    substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    return substrings

#  Get input from the user
text = input("Enter a string: ")

#  Generate and display all substrings
result = all_substrings(text)
print("\nAll substrings:")
for substr in result:
    print(substr)

