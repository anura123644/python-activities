import random
import string

def generate_random_password(length):
    if length < 4:  # Ensure the length is sufficient to include all character types
        return "Password length must be at least 4."
    
    # Character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    
    # Ensure the password includes at least one of each type
    password = random.choice(lower) + random.choice(upper) + random.choice(digits)
    
    # Fill the rest of the password length with random choices
    remaining_length = length - 3
    all_characters = lower + upper + digits
    password += ''.join(random.choices(all_characters, k=remaining_length))
    
    # Shuffle the password to make it more secure
    password = ''.join(random.sample(password, len(password)))
    
    return password

# Example usage
password_length = 12  # You can specify your desired password length
random_password = generate_random_password(password_length)
print("Generated Password:", random_password)
