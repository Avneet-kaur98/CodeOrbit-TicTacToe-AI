"""
CodeOrbit Tech Internship — Project 2: Tic-Tac-Toe with Simple AI

Interactive Tic-Tac-Toe game for Google Colab using ipywidgets.
The computer uses the Minimax algorithm to choose its moves.

Run this source in Google Colab in a code cell, or use the provided
.ipynb notebook for the interactive board.
"""

import math
import ipywidgets as widgets
from IPython.display import display

# X is the human player; O is the computer.
board = [""] * 9
human, computer = "X", "O"
game_over = False


def check_winner(state):
    """Return X/O for a winner, Draw for a full board, or None."""
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]

    for a, b, c in winning_lines:
        if state[a] and state[a] == state[b] == state[c]:
            return state[a]

    return "Draw" if "" not in state else None


def minimax(state, maximizing):
    """
    Recursively evaluate possible moves.
    Computer win = 1, human win = -1, draw = 0.
    """
    result = check_winner(state)

    if result == computer:
        return 1
    if result == human:
        return -1
    if result == "Draw":
        return 0

    if maximizing:
        best_score = -math.inf
        for i in range(9):
            if state[i] == "":
                state[i] = computer
                score = minimax(state, False)
                state[i] = ""
                best_score = max(best_score, score)
        return best_score

    best_score = math.inf
    for i in range(9):
        if state[i] == "":
            state[i] = human
            score = minimax(state, True)
            state[i] = ""
            best_score = min(best_score, score)
    return best_score


def computer_move():
    """Select the computer's best available move using Minimax."""
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == "":
            board[i] = computer
            score = minimax(board, False)
            board[i] = ""

            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board[best_move] = computer


def refresh():
    """Update the board buttons and game status."""
    for i, button in enumerate(buttons):
        button.description = board[i] if board[i] else " "
        button.disabled = bool(board[i]) or game_over

        if board[i] == human:
            button.style.button_color = "#D9EAF7"
        elif board[i] == computer:
            button.style.button_color = "#DDF3E4"
        else:
            button.style.button_color = "#F3F4F6"

    result = check_winner(board)
    if result == human:
        status.value = "<b style='color:green'>You win! 🎉</b>"
    elif result == computer:
        status.value = "<b style='color:#b42318'>Computer wins!</b>"
    elif result == "Draw":
        status.value = "<b>It's a draw!</b>"
    elif not game_over:
        status.value = "<b>Your turn (X)</b>"


def player_move(index):
    """Make a human move and let the computer respond."""
    global game_over

    if game_over or board[index] != "":
        return

    board[index] = human

    if check_winner(board) is not None:
        game_over = True
        refresh()
        return

    computer_move()

    if check_winner(board) is not None:
        game_over = True

    refresh()


# Build a 3x3 grid of interactive buttons.
buttons = []
for index in range(9):
    button = widgets.Button(
        description=" ",
        layout=widgets.Layout(width="85px", height="85px"),
        style={"font_weight": "bold", "font_size": "24px"}
    )
    button.on_click(lambda clicked_button, i=index: player_move(i))
    buttons.append(button)

status = widgets.HTML("<b>Your turn (X)</b>")


def restart_game(_):
    """Reset the board and start a new game."""
    global board, game_over
    board = [""] * 9
    game_over = False
    refresh()


restart_button = widgets.Button(
    description="Restart Game",
    button_style="info",
    icon="refresh"
)
restart_button.on_click(restart_game)

display(widgets.VBox([
    widgets.HTML(
        "<h2 style='color:#12344D'>CodeOrbit Tech — Tic-Tac-Toe AI</h2>"
        "<p>You are X; computer is O. AI uses Minimax.</p>"
    ),
    status,
    widgets.HBox(buttons[0:3]),
    widgets.HBox(buttons[3:6]),
    widgets.HBox(buttons[6:9]),
    restart_button
]))

refresh()
