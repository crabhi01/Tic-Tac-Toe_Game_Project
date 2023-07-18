from tkinter import *
import random


def next_turn(row, column):
    """
    Function to handle the next turn in the game.
    """
    global player

    if buttons[row][column]["text"] == "" and not check_winner():
        buttons[row][column]["text"] = player

        if not check_winner():
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " turn"))
        else:
            label.config(
                text=(players[0] + " wins")
            ) if check_winner() is True else label.config(text="Tie!!!")


def check_winner():
    """
    Function to check if there is a winner in the game.
    """
    for row in range(3):
        if (
            buttons[row][0]["text"]
            == buttons[row][1]["text"]
            == buttons[row][2]["text"]
            != ""
        ):
            for col in range(3):
                buttons[row][col].config(bg="green")
            return True

    for column in range(3):
        if (
            buttons[0][column]["text"]
            == buttons[1][column]["text"]
            == buttons[2][column]["text"]
            != ""
        ):
            for row in range(3):
                buttons[row][column].config(bg="green")
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        for i in range(3):
            buttons[i][i].config(bg="green")
        return True

    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        for i in range(3):
            buttons[i][2 - i].config(bg="green")
        return True

    elif not empty_spaces():
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="red")
        return "Tie"

    else:
        return False


def empty_spaces():
    """
    Function to check if there are any empty spaces left on the board.
    """
    return (
        sum(buttons[row][col]["text"] == "" for row in range(3) for col in range(3)) > 0
    )


def new_game():
    """
    Function to start a new game.
    """
    global player
    player = random.choice(players)
    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="red")


window = Tk()
window.title("Tic-Tac-Toe Game :)")
players = ["#", "*"]
player = random.choice(players)
buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

label = Label(text=player + " turn", font=("consolas", 40))
label.pack(side="top")

reset_button = Button(text="restart", font=("consolas", 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

buttons = [
    [
        Button(
            frame,
            text="",
            font=("consolas", 40),
            width=5,
            height=2,
            command=lambda row=row, column=column: next_turn(row, column),
        )
        for column in range(3)
    ]
    for row in range(3)
]

for row in range(3):
    for column in range(3):
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
"""Lambda functions in Python are anonymous(unnamed) functions that are
  defined without a name. They are primarily used when you need a small, 
  one-line function and don't want to define a separate function using the 'def' keyword. 
  Lambdas are commonly used in functional programming and for creating short, inline functions."""
