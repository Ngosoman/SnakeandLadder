import tkinter as tk
from tkinter import messagebox
import random

BOARD_SIZE = 10
SQUARE_SIZE = 60

# Snakes and ladders
snakes = {
    16: 6,
    48: 30,
    64: 60,
    79: 19,
    93: 68,
    95: 24,
    97: 76,
    98: 78
}

ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}

class SnakesAndLadders:
    def __init__(self, root):
        self.root = root
        self.root.title("🎲 Snakes and Ladders")

        self.canvas = tk.Canvas(root, width=BOARD_SIZE * SQUARE_SIZE, height=BOARD_SIZE * SQUARE_SIZE + 100)
        self.canvas.pack()

        self.draw_board()

        self.player_position = 1
        self.token = None

        self.create_widgets()
        self.draw_token()

    def draw_board(self):
        color = "white"
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x1 = col * SQUARE_SIZE
                y1 = (BOARD_SIZE - 1 - row) * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE

                square_num = self.get_square_number(row, col)
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
                self.canvas.create_text(x1 + SQUARE_SIZE/2, y1 + SQUARE_SIZE/2, text=str(square_num), font=("Arial", 10))

    def get_square_number(self, row, col):
        if row % 2 == 0:
            return row * BOARD_SIZE + col + 1
        else:
            return row * BOARD_SIZE + (BOARD_SIZE - col)

    def get_coords(self, position):
        row = (position - 1) // BOARD_SIZE
        col = (position - 1) % BOARD_SIZE

        if row % 2 == 1:
            col = BOARD_SIZE - 1 - col

        x = col * SQUARE_SIZE + SQUARE_SIZE / 2
        y = (BOARD_SIZE - 1 - row) * SQUARE_SIZE + SQUARE_SIZE / 2
        return x, y

    def draw_token(self):
        if self.token:
            self.canvas.delete(self.token)
        x, y = self.get_coords(self.player_position)
        self.token = self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="blue")

    def create_widgets(self):
        self.roll_button = tk.Button(self.root, text="🎲 Roll Dice", font=("Arial", 14), command=self.roll_dice)
        self.canvas.create_window(150, BOARD_SIZE * SQUARE_SIZE + 50, window=self.roll_button)

        self.dice_label = tk.Label(self.root, text="🎯 Dice: ", font=("Arial", 14))
        self.canvas.create_window(350, BOARD_SIZE * SQUARE_SIZE + 50, window=self.dice_label)

        self.message_label = tk.Label(self.root, text="", font=("Arial", 12), fg="green")
        self.canvas.create_window(550, BOARD_SIZE * SQUARE_SIZE + 50, window=self.message_label)

    def roll_dice(self):
        dice = random.randint(1, 6)
        self.dice_label.config(text=f"🎯 Dice: {dice}")
        new_position = self.player_position + dice

        if new_position > 100:
            self.message_label.config(text="🚫 Can't move. Wait for next roll.")
            return

        # Check for snakes and ladders
        if new_position in snakes:
            final_position = snakes[new_position]
            self.message_label.config(text=f"🐍 Oops! Snake from {new_position} to {final_position}")
            new_position = final_position
        elif new_position in ladders:
            final_position = ladders[new_position]
            self.message_label.config(text=f"🪜 Yay! Ladder from {new_position} to {final_position}")
            new_position = final_position
        else:
            self.message_label.config(text=f"You moved to {new_position}")

        self.player_position = new_position
        self.draw_token()

        if self.player_position == 100:
            messagebox.showinfo("🎉 Game Over", "Congratulations! You reached 100.")
            self.roll_button.config(state=tk.DISABLED)

# Start game
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakesAndLadders(root)
    root.mainloop()
