import tkinter as tk

# Game state
board = [""] * 9
current_player = "X"


def check_winner():
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for combo in wins:
        a, b, c = combo
        if board[a] == board[b] == board[c] != "":
            return combo
    return None


def show_result(message, win_combo=None):
    result_label.config(text=message)

    # Highlight winning cells
    if win_combo:
        for i in win_combo:
            buttons[i].config(bg="lightgreen")

    # Disable all buttons
    for btn in buttons:
        btn.config(state="disabled")

    restart_btn.grid(row=5, column=0, columnspan=3, pady=10)


def restart_game():
    global board, current_player

    board = [""] * 9
    current_player = "X"

    label.config(text=f"Player {current_player}'s turn")
    result_label.config(text="")

    for btn in buttons:
        btn.config(text="", state="normal", bg="SystemButtonFace")

    restart_btn.grid_remove()


def on_click(index):
    global current_player

    if board[index] != "":
        return

    board[index] = current_player
    buttons[index].config(text=current_player)

    win_combo = check_winner()
    if win_combo:
        show_result(f"Player {current_player} wins!", win_combo)
        return

    if "" not in board:
        show_result("It's a draw!")
        return

    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")


# GUI setup
root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(bg="#f0f0f0")

label = tk.Label(root, text=f"Player {current_player}'s turn",
                 font=("Arial", 14), bg="#f0f0f0")
label.grid(row=0, column=0, columnspan=3, pady=10)

buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 18, "bold"),
                    width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=(i//3)+1, column=i%3)
    buttons.append(btn)

result_label = tk.Label(root, text="", font=("Arial", 16),
                        fg="green", bg="#f0f0f0")
result_label.grid(row=4, column=0, columnspan=3)

restart_btn = tk.Button(root, text="Restart Game",
                        command=restart_game)

root.mainloop()