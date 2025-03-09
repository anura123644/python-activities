valid = False
while not valid:  # outer loop for retrying input
    try:
        n = int(input("Enter a number: "))  # prompt for input
        # check if the input is even
        if n % 2 == 0:
            print("bye")
            valid = True  # exit the outer loop
        else:
            print("Please enter an even number.")  # guide the user
    except ValueError:
        print("Invalid input. Please enter a valid number.")  # handle non-integer input
1