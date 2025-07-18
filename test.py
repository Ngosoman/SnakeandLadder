import tkinter as tk
import random

# Constants
BOARD_SIZE = 10
CELL_SIZE = 60
WINDOW_WIDTH = CELL_SIZE * BOARD_SIZE
WINDOW_HEIGHT = CELL_SIZE * BOARD_SIZE + 100

# Start positions
positions = {"red": 0, "blue": 0}

# Initialize window
root = tk.Tk()
root.title("Snakes and Ladders - Setup 1")

# Canvas for board
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()

# Roll dice function
def roll_dice():
    dice = random.randint(1, 6)
    current = player_turn.get()
    positions[current] = min(positions[current] + dice, 99)
    draw_tokens()
    info_label.config(text=f"{current.capitalize()} rolled a {dice}")
    next_turn()