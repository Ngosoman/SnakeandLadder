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

# Draw 10x10 grid
def draw_board():
    number = 100
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x1 = col * CELL_SIZE if row % 2 == 0 else (9 - col) * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
            canvas.create_text(x1 + 30, y1 + 30, text=str(number))
            number -= 1

# Roll dice function
def roll_dice():
    dice = random.randint(1, 6)
    current = player_turn.get()
    positions[current] = min(positions[current] + dice, 99)
    draw_tokens()
    info_label.config(text=f"{current.capitalize()} rolled a {dice}")
    next_turn()