import tkinter as tk
import tkinter as tk
from tkinter import messagebox


def check_winner():
    global winner
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6],             # diagonals
    ]
    for a, b, c in win_combos:
        if buttons[a]["text"] != "" and buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"]:
            buttons[a].config(bg="lightgreen")
            buttons[b].config(bg="lightgreen")
            buttons[c].config(bg="lightgreen")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[a]['text']} wins!")
            return

    if all(btn["text"] != "" for btn in buttons):
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")


def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()


def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")


def reset_game():
    global current_player, winner
    for btn in buttons:
        btn.config(text="", bg="SystemButtonFace")
    current_player = "X"
    winner = False
    label.config(text=f"Player {current_player}'s turn")


root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = []
for i in range(9):
    btn = tk.Button(
        root, text="", font=("Arial", 25), width=6, height=2,
        command=lambda i=i: button_click(i)
    )
    btn.grid(row=i // 3, column=i % 3)
    buttons.append(btn)

current_player = "X"
winner = False

label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Arial", 16))
label.grid(row=3, column=0, columnspan=3)

reset_button = tk.Button(root, text="Reset", font=("Arial", 12), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3, sticky="ew")

root.mainloop()
    
