import tkinter as tk

# Conversion function
def convert():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{inches} inches = {cm:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Creating the main window
root = tk.Tk()
root.title("Length Converter")

# Input field
tk.Label(root, text="Enter length in inches:").pack()
entry = tk.Entry(root)
entry.pack()

# Convert button
tk.Button(root, text="Convert", command=convert).pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

