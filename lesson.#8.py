# Program to calculate customer due amount

# Input: Total bill amount
total_bill = float(input("Enter the total bill amount: "))

# Input: Amount paid by the customer
amount_paid = float(input("Enter the amount paid by the customer: "))

# Calculate the due amount
due_amount = total_bill - amount_paid

# Display the result
if due_amount > 0:
    print(f"The due amount is: {due_amount}")
elif due_amount == 0:
    print("The bill is fully paid. No due amount.")
else:
    print(f"The customer has overpaid by {-due_amount}.")
