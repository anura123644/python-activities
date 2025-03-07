def check_age():
    try:
        # Get input from the user
        age = int(input("Please enter your age: "))

        # Check if the age is within a reasonable range
        if age < 0 or age > 120:
            print("The age entered is not valid.")
        else:
            print("The age entered is valid.")

            # Check if the age is even or odd
            if age % 2 == 0:
                print("The age entered is even.")
            else:
                print("The age entered is odd.")
    
    except ValueError:
        print("Please enter a valid integer for age.")

# Call the function
check_age()
