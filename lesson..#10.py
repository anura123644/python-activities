def check_age():
    try:
        # Get user input
        age = int(input("Enter your age: "))

        # Validate the age
        if age < 0:
            print("Error: Age cannot be negative. Please enter a valid age.")
        else:
            # Check if age is even or odd
            if age % 2 == 0:
                print(f"The entered age {age} is even.")
            else:
                print(f"The entered age {age} is odd.")
    except ValueError:
        # Handle non-integer input
        print("Error: Please enter a valid integer value for age.")

# Call the function
check_age()

