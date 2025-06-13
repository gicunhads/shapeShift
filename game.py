import random
from pieces import Piece, Color, Shape, Size
from board import Board

class Game:
    def __init__(self):
        # 5×5 board instance
        self.board = Board()

        # Pool of 8 unique pieces: each Color × Shape × Size
        self.pool = self._generate_pool()

        # Holds the piece drawn but not yet placed
        self.drawn_piece = None

    def _generate_pool(self):
        """Create one of each combination of color, shape, and size."""
        pool = [
            Piece(color, shape, size)
            for color in (Color.BLACK, Color.WHITE)
            for shape in (Shape.HEART, Shape.TRIANGLE)
            for size in (Size.BIG, Size.SMALL)
        ]
        random.shuffle(pool)
        return pool

    def print_board(self):
        """Display the current board in text form."""
        self.board.print_board()

    def start_draw(self):
        """
        Draw one piece from the pool.
        Returns (piece, message). On empty pool, piece is None.
        """
        if not self.pool:
            return None, "No pieces left to draw."
        self.drawn_piece = self.pool.pop()
        return self.drawn_piece, f"Drawn piece: {self.drawn_piece}"

    def place_drawn_piece(self, row, col):
        """
        Place the previously drawn piece at (row, col).
        Returns (success, message).
        """
        if self.drawn_piece is None:
            return False, "No piece drawn to place."
        success = self.board.place_piece(row, col, self.drawn_piece)
        if not success:
            return False, "Invalid placement."
        self.drawn_piece = None
        return True, "Piece placed."

    def move_piece(self, fr, fc, tr, tc):
        """
        Move a piece on the board from (fr, fc) to (tr, tc).
        Returns (success, message).
        """
        success = self.board.move_piece(fr, fc, tr, tc)
        return (True, "Piece moved.") if success else (False, "Invalid move.")

    def check_win(self):
        """
        Check the board for any win condition of 4 in-line pieces.
        Returns (True, reason) or (False, "").
        """
        # Detect lines of 4 matching attributes
        return self.board.check_win(N=4)
