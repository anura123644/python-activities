import random
import string
import tkinter as tk

def generate_password():
    length = 12  # You can change this to any length
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Creating the Tkinter window
root = tk.Tk()
root.title("Random Password Generator")

password_var = tk.StringVar()

frame = tk.Frame(root)
frame.pack(pady=10)

label = tk.Label(frame, text="Generated Password:")
label.pack()

password_entry = tk.Entry(frame, textvariable=password_var, width=30)
password_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

root.mainloop()

