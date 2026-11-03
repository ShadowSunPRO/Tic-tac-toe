import tkinter as tk

Name=input("Как вас зовут?")
window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("630x750")
window.resizable(False, False)

current_player = "X"
score_x = 0
score_o = 0
game_running = True

name_label=tk.Label(
    window,
    text=Name,
    font=("Arial", 30,"bold")

)
name_label.pack(pady=30)


title_label = tk.Label(window, text="КРЕСТИКИ-НОЛИКИ", font=("Arial", 24, "bold"))
title_label.pack(pady=15)

turn_label = tk.Label(window, text="Ход игрока: X", font=("Arial", 16, "bold"))
turn_label.pack()

score_label = tk.Label(window, text="X: 0     O: 0", font=("Arial", 14))
score_label.pack(pady=10)

game_frame = tk.Frame(window)
game_frame.pack(pady=10)

buttons = []


def check_winner():
    combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for a, b, c in combinations:
        if (
            buttons[a]["text"] != ""
            and buttons[a]["text"] == buttons[b]["text"]
            and buttons[a]["text"] == buttons[c]["text"]
        ):
            return (a, b, c)

    return None


def check_draw():
    for button in buttons:
        if button["text"] == "":
            return False
    return True


def button_click(index):
    global current_player, game_running, score_x, score_o

    if not game_running:
        return

    if buttons[index]["text"] != "":
        return

    if current_player == "X":
        buttons[index].config(text="X", fg="blue")
    else:
        buttons[index].config(text="O", fg="red")

    winner = check_winner()

    if winner is not None:
        game_running = False

        for winner_index in winner:
            buttons[winner_index].config(bg="#90EE90")

        turn_label.config(text=f"Победил игрок {current_player}!")

        if current_player == "X":
            score_x += 1
        else:
            score_o += 1

        score_label.config(text=f"X: {score_x}     O: {score_o}")
        return

    if check_draw():
        game_running = False
        turn_label.config(text="Ничья!")
        return

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    turn_label.config(text=f"Ход игрока: {current_player}")


for index in range(9):
    button = tk.Button(
        game_frame,
        text="",
        font=("Arial", 30, "bold"),
        width=4,
        height=2,
        bg="#eeeeee",
        command=lambda i=index: button_click(i)
    )

    row = index // 3
    column = index % 3
    button.grid(row=row, column=column, padx=3, pady=3)
    buttons.append(button)


def restart_game():
    global current_player, game_running

    current_player = "X"
    game_running = True
    turn_label.config(text="Ход игрока: X")

    for button in buttons:
        button.config(text="", fg="black", bg="#eeeeee")


restart_button = tk.Button(
    window,
    text="Новая игра",
    font=("Arial", 14, "bold"),
    command=restart_game,
    bg="#87CEEB"
)
restart_button.pack(pady=15)

window.mainloop()