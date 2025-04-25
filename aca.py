import tkinter as tk
from datetime import datetime

# Function to calculate age
def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        birth_date = datetime(year, month, day)
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        result_label.config(text=f"Your age: {age} years")
    except ValueError:
        result_label.config(text="Please enter a valid date")

# Creating the main window
root = tk.Tk()
root.title("Age Calculator")

# Labels and Entry fields
tk.Label(root, text="Enter your date of birth:").grid(row=0, columnspan=2)

tk.Label(root, text="Day:").grid(row=1, column=0)
day_entry = tk.Entry(root)
day_entry.grid(row=1, column=1)

tk.Label(root, text="Month:").grid(row=2, column=0)
month_entry = tk.Entry(root)
month_entry.grid(row=2, column=1)

tk.Label(root, text="Year:").grid(row=3, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=3, column=1)

# Calculate button
tk.Button(root, text="Calculate Age", command=calculate_age).grid(row=4, columnspan=2)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=5, columnspan=2)

root.mainloop()

