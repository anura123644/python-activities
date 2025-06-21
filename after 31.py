import tkinter as tk
import random

def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result.set(f"Tie! Both chose {user_choice}")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result.set(f"You Win! Computer chose {computer_choice}")
    else:
        result.set(f"You Lose! Computer chose {computer_choice}")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("300x300")

result = tk.StringVar()
tk.Label(root, text="Choose Rock, Paper or Scissors:").pack(pady=10)

# Buttons
tk.Button(root, text="Rock", width=10, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=10, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors")).pack(pady=5)

tk.Label(root, textvariable=result, wraplength=250, font=("Arial", 12)).pack(pady=20)

root.mainloop()

