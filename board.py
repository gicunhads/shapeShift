from pieces import Piece, Color, Shape, Size

class Board:
    def __init__(self, size=5):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]

    def is_empty(self, row, col):
        return self.grid[row][col] is None

    def place_piece(self, row, col, piece: Piece) -> bool:
        if not (0 <= row < self.size and 0 <= col < self.size):
            return False
        if self.grid[row][col] is not None:
            return False
        self.grid[row][col] = piece
        return True

    def move_piece(self, fr, fc, tr, tc) -> bool:
        if not self.valid_move(fr, fc, tr, tc):
            return False
        self.grid[tr][tc] = self.grid[fr][fc]
        self.grid[fr][fc] = None
        return True

    def valid_move(self, fr, fc, tr, tc) -> bool:
        if not (0 <= fr < self.size and 0 <= fc < self.size):
            return False
        if not (0 <= tr < self.size and 0 <= tc < self.size):
            return False
        piece = self.grid[fr][fc]
        if piece is None:
            return False
        if self.grid[tr][tc] is not None:
            return False  # no jumping on occupied cell
        dr = tr - fr
        dc = tc - fc

        dist = max(abs(dr), abs(dc))
        if piece.size == Size.SMALL and dist != 1:
            return False
        if piece.size == Size.BIG and (dist != 3):
            return False

        # Movement by shape
        if piece.shape == Shape.HEART:
            if abs(dr) != abs(dc):
                return False
        elif piece.shape == Shape.TRIANGLE:
            if dr != 0 and dc != 0:
                return False
        else:
            return False

        # Path clearance
        step_r = (dr // abs(dr)) if dr != 0 else 0
        step_c = (dc // abs(dc)) if dc != 0 else 0
        r, c = fr + step_r, fc + step_c
        while (r, c) != (tr, tc):
            if self.grid[r][c] is not None:
                return False
            r += step_r
            c += step_c
        return True

    def print_board(self):
        for row in self.grid:
            print(" | ".join([str(p) if p else " . " for p in row]))

    def check_win(self, N=3):
        lines = []

        # Rows and cols
        for i in range(self.size):
            lines.append(self.grid[i])  # row
            lines.append([self.grid[r][i] for r in range(self.size)])  # col

        # Diagonals
        for r in range(self.size - N + 1):
            diag1 = [self.grid[r + i][i] for i in range(self.size - r)]
            diag2 = [self.grid[i][r + i] for i in range(self.size - r)]
            lines.append(diag1)
            lines.append(diag2)

        for line in lines:
            for start in range(len(line) - N + 1):
                segment = line[start:start + N]
                if None in segment:
                    continue
                if all(p.shape == segment[0].shape for p in segment):
                    return True, f"Win by shape {segment[0].shape.value}"
                if all(p.size == segment[0].size for p in segment):
                    return True, f"Win by size {segment[0].size.value}"
                if all(p.color == segment[0].color for p in segment):
                    return True, f"Win by color {segment[0].color.value}"
        return False, ""
