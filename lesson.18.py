def is_alphabet(char):
    if char.isalpha():
        return True
    else:
        return False

# Example usage
character = input("Enter a character: ")

if is_alphabet(character):
    print(f"'{character}' is an alphabet.")
else:
    print(f"'{character}' is not an alphabet.")
