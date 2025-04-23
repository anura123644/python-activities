import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        # Simple Interest formula
        simple_interest = (principal * rate * time) / 100
        
        # Compound Interest formula
        compound_interest = principal * ((1 + rate / 100) ** time) - principal
        
        result = f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}"
        messagebox.showinfo("Interest Results", result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numerical values.")

# Tkinter Window
window = tk.Tk()
window.title("Interest Calculator")

# Labels and Input Fields
tk.Label(window, text="Principal Amount:").grid(row=0, column=0, padx=10, pady=10)
entry_principal = tk.Entry(window)
entry_principal.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Rate of Interest (%):").grid(row=1, column=0, padx=10, pady=10)
entry_rate = tk.Entry(window)
entry_rate.grid(row=1, column=1, padx=10, pady=10)

tk.Label(window, text="Time Period (years):").grid(row=2, column=0, padx=10, pady=10)
entry_time = tk.Entry(window)
entry_time.grid(row=2, column=1, padx=10, pady=10)

# Calculate Button
btn_calculate = tk.Button(window, text="Calculate Interest", command=calculate_interest)
btn_calculate.grid(row=3, columnspan=2, pady=20)

window.mainloop()

