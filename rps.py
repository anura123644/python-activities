import random
import tkinter as tk
from tkinter import messagebox

# Function to determine the winner
def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result = ""
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    messagebox.showinfo("Result", f"You chose {user_choice}\nComputer chose {computer_choice}\n\n{result}")

# Creating the Tkinter window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Adding buttons for user choices
tk.Label(root, text="Choose:").pack()

tk.Button(root, text="Rock", command=lambda: play("Rock")).pack()
tk.Button(root, text="Paper", command=lambda: play("Paper")).pack()
tk.Button(root, text="Scissors", command=lambda: play("Scissors")).pack()

root.mainloop()

