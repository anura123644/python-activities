import tkinter as tk

# Function to calculate the product
def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Creating the main window
root = tk.Tk()
root.title("Multiplication App")

# Labels and Entry fields
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Calculate button
tk.Button(root, text="Multiply", command=multiply).pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

