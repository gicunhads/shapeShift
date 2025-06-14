import tkinter as tk
from game import Game
from pieces import Color, Shape, Size

CELL_SIZE = 80  # pixels per cell
BOARD_SIZE = 5  # 5x5 grid



# Emoji mapping
def piece_to_emoji(piece):
    if piece is None:
        return ""
    if piece.color == Color.BLACK:
        if piece.shape == Shape.HEART:
            return "🖤" if piece.size == Size.BIG else "♥︎"
        else:
            return "⬛️" if piece.size == Size.BIG else "▪️"
    else:
        if piece.shape == Shape.HEART:
            return "🤍" if piece.size == Size.BIG else "♡"
        else:
            return "⬜️" if piece.size == Size.BIG else "▫️"

class ShapeshiftCanvasGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Shapeshift - Canvas GUI")
        self.game = Game()
        self.action = None       # 'draw', 'move', or None
        self.drawn_piece = None  # holds drawn but unplaced piece
        self.selected = None     # (row, col) of piece to move
        self.game_over = False
        # Info label
        self.info = tk.Label(master, text="Click 'Draw Piece' or 'Move Piece' to begin.")
        self.info.pack(pady=5)

        # Control buttons frame
        ctrl = tk.Frame(master)
        ctrl.pack()
        tk.Button(ctrl, text="Draw Piece", command=self.start_draw).pack(side="left", padx=5)
        tk.Button(ctrl, text="Move Piece", command=self.start_move).pack(side="left", padx=5)
        tk.Button(ctrl, text="Restart", command=self.restart_game).pack(side="left", padx=5)
        # Canvas for board grid
        canvas_size = CELL_SIZE * BOARD_SIZE
        self.canvas = tk.Canvas(master, width=canvas_size, height=canvas_size)
        self.canvas.pack(pady=10)
        self.canvas.bind("<Button-1>", self.on_click)
        

        self.draw_board()
        self.update_display()

    def draw_board(self):
        # Draw grid lines
        self.canvas.delete("grid")
        for i in range(BOARD_SIZE + 1):
            x = i * CELL_SIZE
            y = i * CELL_SIZE
            self.canvas.create_line(x, 0, x, BOARD_SIZE * CELL_SIZE, tags="grid")
            self.canvas.create_line(0, y, BOARD_SIZE * CELL_SIZE, y, tags="grid")


    def update_display(self):
    # Draw pieces
        self.canvas.delete("piece")
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                p = self.game.board.grid[r][c]
                em = piece_to_emoji(p)
                if em:
                    cx = c * CELL_SIZE + CELL_SIZE/2
                    cy = r * CELL_SIZE + CELL_SIZE/2
                    self.canvas.create_text(cx, cy, text=em, font=("Arial", 32), tags="piece")

        # Only overwrite the info label if the game isn't already over
        if not self.game_over and self.action is None:
            self.info.config(text=f"Pieces left: {len(self.game.pool)}")

        # Immediately check for win and lock the board if needed
        if not self.game_over:
            win, reason = self.game.check_win()
            if win:
                self.game_over = True
                self.info.config(text=f"Game Over! {reason}")
                self.canvas.unbind("<Button-1>")

    def restart_game(self):
        """Reset the game to initial state."""
        self.game = Game()
        self.game_over = False
        self.action = None
        self.drawn_piece = None
        self.selected = None
        # Redraw board and re-enable input
        self.draw_board()
        self.update_display()
        self.canvas.bind("<Button-1>", self.on_click)
        self.info.config(text="Game restarted. Click 'Draw Piece' or 'Move Piece' to begin.")

    def start_draw(self):
        piece, msg = self.game.start_draw()
        if piece:
            self.action = 'draw'
            self.drawn_piece = piece
            self.info.config(text=f"Drawn: {piece_to_emoji(piece)} - click cell to place.")
        else:
            self.info.config(text=msg)
        self.update_display()

    def start_move(self):
        self.action = 'move'
        self.selected = None
        self.info.config(text="Move mode: select a piece to move.")
        self.update_display()

    def on_click(self, event):
        if self.game_over:
            return

        row = event.y // CELL_SIZE
        col = event.x // CELL_SIZE
        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
            return


        # Explicit draw mode
        if self.action == 'draw':
            if self.drawn_piece:
                success, msg = self.game.place_drawn_piece(row, col)
                self.info.config(text=msg)
                if success:
                    self.action = None
                    self.drawn_piece = None
                    # After placing the very last piece, auto-enter move mode
                    if not self.game.pool:
                        self.action = 'move'
                        self.info.config(text="All pieces placed! Now select a piece to move.")
                self.update_display()
            return

        # Move mode
        if self.action == 'move':
            # First click: select a piece
            if self.selected is None:
                if self.game.board.grid[row][col] is None:
                    self.info.config(text="No piece here to select.")
                else:
                    self.selected = (row, col)
                    self.info.config(text=f"Selected ({row},{col}). Click destination.")
                return

            # Second click: perform the move
            fr, fc = self.selected
            success, msg = self.game.move_piece(fr, fc, row, col)
            self.info.config(text=msg)
            if success:
                self.action = None
                self.selected = None
            self.update_display()
            return


    def draw_cell_empty(self, r, c):
            return self.game.board.grid[r][c] is None

if __name__ == '__main__':
    root = tk.Tk()
    ShapeshiftCanvasGUI(root)
    root.mainloop()
