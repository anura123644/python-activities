import tkinter as tk
from tkinter import ttk

def check_password_strength():
    password = password_entry.get()
    length = len(password)

    if length < 8:
        strength = "Weak"
    elif length < 12:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    result_label.config(text=f"Password Strength: {strength}")

window = tk.Tk()
window.title("Password Strength Checker")

password_label = ttk.Label(window, text="Enter Password:")
password_label.pack()

password_entry = ttk.Entry(window, show="*")
password_entry.pack()

check_button = ttk.Button(window, text="Check Strength", command=check_password_strength)
check_button.pack()

result_label = ttk.Label(window, text="")
result_label.pack()

window.mainloop()
