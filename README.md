# CodeOrbit Tech Internship — Project 2: Tic-Tac-Toe with Simple AI

## Overview
This is an interactive Tic-Tac-Toe game where a human player (X) plays against the computer (O). The computer uses the Minimax algorithm to choose its moves.

## Features
- Interactive 3×3 game board
- Human vs. computer gameplay
- Minimax AI opponent
- Win, loss, and draw detection
- Restart Game button
- Beginner-friendly, commented Python code
- Google Colab-compatible interface using `ipywidgets`

## Technologies
- Python
- Minimax algorithm
- ipywidgets
- Google Colab

## How to Run
1. Open [Google Colab](https://colab.research.google.com/).
2. Upload and open `CodeOrbit_TicTacToe_AI.ipynb` using **File → Upload notebook**.
3. Run the code cell.
4. Click a square to play as **X**. The computer plays as **O**.
5. Click **Restart Game** to begin a new game.

The provided `.ipynb` notebook is the recommended way to run the interactive interface in Colab. The `.py` file contains the same source code for review and GitHub submission.

## How Minimax Works
Minimax explores possible future game moves:
- Computer win: score `1`
- Human win: score `-1`
- Draw: score `0`

The computer chooses the move with the highest score. With optimal play, it should not lose.

## Project Files
- `tictactoe_ai.py` — Python source code
- `README.md` — project documentation
- `CodeOrbit_TicTacToe_AI.ipynb` — Google Colab notebook

