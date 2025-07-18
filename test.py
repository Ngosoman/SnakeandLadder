import tkinter as tk
import random

# Constants
BOARD_SIZE = 10
CELL_SIZE = 60
WINDOW_WIDTH = CELL_SIZE * BOARD_SIZE
WINDOW_HEIGHT = CELL_SIZE * BOARD_SIZE + 100  # extra height for controls

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

# Get x, y from position (0–99)
def get_coordinates(position):
    row = 9 - (position // 10)
    col = position % 10 if (row % 2 == 0) else 9 - (position % 10)
    x = col * CELL_SIZE + CELL_SIZE // 2
    y = row * CELL_SIZE + CELL_SIZE // 2
    return x, y

# Draw tokens
tokens = {}
def draw_tokens():
    for color in ["red", "blue"]:
        x, y = get_coordinates(positions[color])
        if color in tokens:
            canvas.delete(tokens[color])
        tokens[color] = canvas.create_oval(x-15, y-15, x+15, y+15, fill=color)

# Turn tracker
player_turn = tk.StringVar(value="red")

# Turn switch
def next_turn():
    player_turn.set("blue" if player_turn.get() == "red" else "red")

# Dice roll
# def roll_dice():
#     dice = random.randint(1, 6)
#     current = player_turn.get()
#     positions[current] = min(positions[current] + dice, 99)
#     draw_tokens()
#     info_label.config(text=f"{current.capitalize()} rolled a {dice}")
#     next_turn()

# Draw board & tokens
draw_board()
draw_tokens()

# Dice Button
dice_button = tk.Button(root, text="Roll Dice", command=roll_dice, font=("Arial", 16))
dice_button.pack(pady=10)

# Info Label
info_label = tk.Label(root, text="Red starts!", font=("Arial", 14))
info_label.pack()

# Run app
root.mainloop()


# ladders and snakes
ladders = {
    3: 22,
    5: 8,
    11: 26,
    20: 29,
    27: 56,
    21: 82,
}

snakes = {
    17: 4,
    19: 7,
    23: 15,
    54: 34,
    62: 18,
    87: 24,
    99: 2,
}
