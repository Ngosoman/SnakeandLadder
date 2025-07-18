import tkinter as tk
import random

# Roll dice function
def roll_dice():
    dice = random.randint(1, 6)
    current = player_turn.get()
    positions[current] = min(positions[current] + dice, 99)
    draw_tokens()
    info_label.config(text=f"{current.capitalize()} rolled a {dice}")
    next_turn()