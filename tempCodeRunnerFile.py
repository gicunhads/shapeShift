
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
