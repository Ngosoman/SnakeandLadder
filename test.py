import tkinter as tk
from tkinter import messagebox
import random

BOARD_SIZE = 10
SQUARE_SIZE = 60

snakes = {
    16: 6, 48: 30, 64: 60, 79: 19,
    93: 68, 95: 24, 97: 76, 98: 78
}

ladders = {
    1: 38, 4: 14, 9: 31, 21: 42,
    28: 84, 36: 44, 51: 67, 71: 91, 80: 100
}

class SnakesAndLadders:
    def __init__(self, root):
        self.root = root
        self.root.title("Snakes and Ladders - 2 Player")

        self.canvas = tk.Canvas(root, width=BOARD_SIZE * SQUARE_SIZE, height=BOARD_SIZE * SQUARE_SIZE + 100)
        self.canvas.pack()

        self.draw_board()

        self.player_positions = [1, 1]
        self.tokens = [None, None]
        self.current_player = 0  # 0: Player 1, 1: Player 2

        self.create_widgets()
        self.draw_tokens()

    def draw_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x1 = col * SQUARE_SIZE
                y1 = (BOARD_SIZE - 1 - row) * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE

                square_num = self.get_square_number(row, col)
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="burlywood", outline="black")
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

    def draw_tokens(self):
        colors = ["blue", "red"]
        for i in range(2):
            if self.tokens[i]:
                self.canvas.delete(self.tokens[i])
            x, y = self.get_coords(self.player_positions[i])
            offset = -10 if i == 0 else 10  # offset tokens slightly to avoid overlap
            self.tokens[i] = self.canvas.create_oval(
                x - 10 + offset, y - 10, x + 10 + offset, y + 10, fill=colors[i]
            )

    def create_widgets(self):
        self.roll_button = tk.Button(self.root, text="Roll Dice", font=("Arial", 14), command=self.roll_dice)
        self.canvas.create_window(150, BOARD_SIZE * SQUARE_SIZE + 50, window=self.roll_button)

        self.dice_label = tk.Label(self.root, text=" Dice: ", font=("Arial", 14))
        self.canvas.create_window(350, BOARD_SIZE * SQUARE_SIZE + 50, window=self.dice_label)

        self.message_label = tk.Label(self.root, text="Player 1's Turn", font=("Arial", 12), fg="green")
        self.canvas.create_window(550, BOARD_SIZE * SQUARE_SIZE + 50, window=self.message_label)

    def roll_dice(self):
        dice = random.randint(1, 6)
        self.dice_label.config(text=f"Dice: {dice}")
        pos = self.player_positions[self.current_player]
        new_pos = pos + dice

        if new_pos > 100:
            self.message_label.config(text=f"Player {self.current_player + 1}: Can't move. Wait for next roll.")
            self.switch_turn()
            return

        # Check for snake or ladder
        if new_pos in snakes:
            final = snakes[new_pos]
            msg = f"😬 Snake! Player {self.current_player + 1} drops from {new_pos} to {final}"
            new_pos = final
        elif new_pos in ladders:
            final = ladders[new_pos]
            msg = f"🎉 Ladder! Player {self.current_player + 1} climbs from {new_pos} to {final}"
            new_pos = final
        else:
            msg = f"Player {self.current_player + 1} moved to {new_pos}"

        self.player_positions[self.current_player] = new_pos
        self.draw_tokens()

        if new_pos == 100:
            messagebox.showinfo("🏆 Game Over", f"🎉 Player {self.current_player + 1} wins!")
            self.roll_button.config(state=tk.DISABLED)
            return

        self.message_label.config(text=msg)
        self.switch_turn()

    def switch_turn(self):
        self.current_player = 1 - self.current_player
        self.message_label.config(text=f"Player {self.current_player + 1}'s Turn")

# Launch the game
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakesAndLadders(root)
    root.mainloop()
