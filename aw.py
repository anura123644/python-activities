import tkinter as tk
import random

def play(choice):
    comp = random.choice(['Rock', 'Paper', 'Scissors'])
    if choice == comp:
        result = "Tie!"
    elif (choice == 'Rock' and comp == 'Scissors') or \
         (choice == 'Paper' and comp == 'Rock') or \
         (choice == 'Scissors' and comp == 'Paper'):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    result_lbl.config(text=f"Computer: {comp}\n{result}")

root = tk.Tk()
root.title("RPS Game")
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 14)).pack(pady=10)

for i, move in enumerate(['Rock', 'Paper', 'Scissors']):
    tk.Button(root, text=move, width=10, command=lambda m=move: play(m)).pack(pady=2)

result_lbl = tk.Label(root, text="", font=("Arial", 12))
result_lbl.pack(pady=20)

root.mainloop()


