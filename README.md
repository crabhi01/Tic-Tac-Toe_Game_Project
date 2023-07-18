# Tic-Tac-Toe_Game_Project
This project is a simple implementation of a Tic-Tac-Toe game using the Tkinter library in Python. Tkinter is a standard GUI toolkit for Python, and it provides the necessary components for creating graphical user interfaces.

The game starts by displaying a window with a grid of buttons representing the Tic-Tac-Toe board. Two players take turns clicking on the buttons to make their moves. The current player's turn is indicated at the top of the window.

The `next_turn` function handles the logic for each player's turn. When a button is clicked, it checks if the button is empty and there is no winner yet. If the conditions are met, it updates the button with the current player's symbol ('#' or '*'). Then, it checks for a winner using the `check_winner` function.

The `check_winner` function examines the board state to determine if there is a winning condition. It checks for three in a row horizontally, vertically, and diagonally. If a winner is found, the winning buttons are highlighted with a green background. If all spaces are filled and no winner is found, it declares a tie.

The `empty_spaces` function checks if there are any empty spaces left on the board by counting the number of buttons with an empty text.

The `new_game` function resets the game by randomly choosing the starting player, updating the label at the top of the window, and clearing the board.

Overall, this project demonstrates the use of Tkinter for creating a graphical game interface and implementing the logic for a simple game like Tic-Tac-Toe.
