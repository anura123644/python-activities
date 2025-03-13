# Get age input from the user
age = int(input("Enter your age: "))

# Check if the age is between 10 and 20
if age >= 10:
    if age <= 20:
        print("Your age is between 10 and 20 years.")
    else:
        print("Your age is greater than 20 years.")
else:
    print("Your age is less than 10 years.")
