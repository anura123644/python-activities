import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Set maximum attempts
max_attempts = 3

print("I'm thinking of a number between 1 and 10. Can you guess it?")
print(f"You have {max_attempts} attempts.")

for attempt in range(1, max_attempts + 1):
    try:
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempt} attempts.")
            break
    except ValueError:
        print("Please enter a valid number.")

    if attempt == max_attempts:
        print(f"Sorry, you've run out of attempts. The number was {secret_number}.")

