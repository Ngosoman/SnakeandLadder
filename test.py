import tkinter as tk
import random

# Constants
BOARD_SIZE = 10
CELL_SIZE = 60
WINDOW_WIDTH = CELL_SIZE * BOARD_SIZE
WINDOW_HEIGHT = CELL_SIZE * BOARD_SIZE + 100

# Player positions
positions = {"red": 0, "blue": 0}

# Snakes and ladders
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

# Initialize window
root = tk.Tk()
root.title("Snakes and Ladders")

canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()

# Draw board grid with numbers
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

# Get pixel coordinates from position
def get_coordinates(position):
    row = 9 - (position // 10)
    col = position % 10 if (row % 2 == 0) else 9 - (position % 10)
    x = col * CELL_SIZE + CELL_SIZE // 2
    y = row * CELL_SIZE + CELL_SIZE // 2
    return x, y

# Draw tokens on board
tokens = {}
def draw_tokens():
    for color in ["red", "blue"]:
        x, y = get_coordinates(positions[color])
        if color in tokens:
            canvas.delete(tokens[color])
        tokens[color] = canvas.create_oval(x-15, y-15, x+15, y+15, fill=color)

# Turn control
player_turn = tk.StringVar(value="red")

def next_turn():
    player_turn.set("blue" if player_turn.get() == "red" else "red")

# Dice roll and move logic
def roll_dice():
    dice = random.randint(1, 6)
    current = player_turn.get()
    old_position = positions[current]
    new_position = min(old_position + dice, 99)

    print(f"{current} rolled {dice} and moved from {old_position} to {new_position}")

    # Ladder check
    if new_position in ladders:
        info_label.config(text=f"{current.capitalize()} rolled {dice} 🎲 and climbed a ladder! ⬆️")
        print(f"LADDER: {current} goes from {new_position} to {ladders[new_position]}")
        new_position = ladders[new_position]

    # Snake check
    elif new_position in snakes:
        info_label.config(text=f"{current.capitalize()} rolled {dice} 🎲 and got bitten by a snake! 🐍")
        print(f"SNAKE: {current} goes from {new_position} to {snakes[new_position]}")
        new_position = snakes[new_position]

    else:
        info_label.config(text=f"{current.capitalize()} rolled a {dice}")

    positions[current] = new_position
    draw_tokens()

    if new_position == 99:
        info_label.config(text=f"{current.capitalize()} wins! 🎉")
        dice_button.config(state="disabled")
    else:
        next_turn()

# Reset game
def reset_game():
    positions["red"] = 0
    positions["blue"] = 0
    player_turn.set("red")
    draw_tokens()
    info_label.config(text="Game reset! Red starts.")
    dice_button.config(state="normal")

# UI
draw_board()
draw_tokens()

dice_button = tk.Button(root, text="Roll Dice", command=roll_dice, font=("Arial", 16))
dice_button.pack(pady=5)

info_label = tk.Label(root, text="Red starts!", font=("Arial", 14))
info_label.pack()

reset_button = tk.Button(root, text="Reset Game", command=reset_game, font=("Arial", 12))
reset_button.pack()

# Launch app
root.mainloop()
