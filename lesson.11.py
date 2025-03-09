try:
    # Take two numbers as input, separated by a comma
    num1, num2 = eval(input("Enter two numbers, separated by a comma: "))
    # Perform division
    result = num1 / num2
    print("Result is", result)
# Handle division by zero
except ZeroDivisionError:
    print("Division by zero is an error!")
# Handle incorrect input format, such as missing a comma
except SyntaxError:
    print("Comma is missing. Enter numbers separated by a comma, like this: 1, 2")
# Handle any other type of error
except:
    print("Wrong input!")
# Execute if there are no exceptions
else:
    print("No exceptions occurred.")
# Always execute this block
finally:
    print("This will execute no matter what.")
