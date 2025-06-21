#Write a Python program to create a Denominator Calculator to calculate the number of notes of denominations - 2000, 500, and 100 for the amount entered by the user. and create its GUI for the user by using the Tkinter library.
import tkinter as tk
from tkinter import messagebox

def calculate_notes():
    try:
        amount = int(entry_amount.get())
        if amount % 100 != 0:
            messagebox.showerror("Invalid Amount", "Amount must be a multiple of 100")
            return

        notes_2000 = amount // 2000
        remainder = amount % 2000

        notes_500 = remainder // 500
        remainder %= 500

        notes_100 = remainder // 100

        label_result.config(text=f"2000 x {notes_2000}\n500 x {notes_500}\n100 x {notes_100}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

# Create GUI window
root = tk.Tk()
root.title("Denomination Calculator")

# Create widgets
tk.Label(root, text="Enter the amount:").pack(pady=10)
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Button(root, text="Calculate", command=calculate_notes).pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Run the application
root.mainloop()

