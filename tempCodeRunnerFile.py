def on_click(self, event):
        row = int(event.y // CELL_SIZE)
        col = int(event.x // CELL_SIZE)
        if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
            return

    # If no action selected, treat click on empty cell as draw+place
        if self.action is None:
            if self.game.pool:
                # automatically draw then place
                piece, draw_msg = self.game.start_draw()
                if piece is None:
                    self.info.config(text=draw_msg)
                else:
                    placed, place_msg = self.game.place_drawn_piece(row, col)
                    # show draw then place feedback
                    self.info.config(text=place_msg)
                self.update_display()
                return
            else:
                self.info.config(text="No pieces left to draw. Choose Move to move pieces.")
                return

        if self.action == 'draw':
            success, msg = self.game.place_drawn_piece(row, col)
            self.info.config(text=msg)
            if success:
                self.action = None
                self.drawn_piece = None
            self.update_display()

        elif self.action == 'move':
            # First click: select piece
            if self.selected is None:
                if self.game.board.grid[row][col] is None:
                    self.info.config(text="No piece here. Select a non-empty cell.")
                else:
                    self.selected = (row, col)
                    self.info.config(text=f"Selected piece at ({row},{col}). Now click destination.")
                return
            # Second click: move piece
            fr, fc = self.selected
            success, msg = self.game.move_piece(fr, fc, row, col)
            self.info.config(text=msg)
            # Reset selection on success
            if success:
                self.selected = None
                self.action = None
            # Check win
            win, reason = self.game.check_win()
            if win:
                self.info.config(text=f"Game Over! {reason}")
                # disable canvas clicks
                self.canvas.unbind("<Button-1>")
            self.update_display()

        else:
            self.info.config(text="Choose 'Draw Piece' or 'Move Piece' first.")
            row = int(event.y // CELL_SIZE)
            col = int(event.x // CELL_SIZE)
            if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
                return

        if self.action == 'draw':
            success, msg = self.game.place_drawn_piece(row, col)
            self.info.config(text=msg)
            if success:
                self.action = None
                self.drawn_piece = None
            self.update_display()

        elif self.action == 'move':
            # First click: select piece
            if self.selected is None:
                if self.game.board.grid[row][col] is None:
                    self.info.config(text="No piece here. Select a non-empty cell.")
                else:
                    self.selected = (row, col)
                    self.info.config(text=f"Selected piece at ({row},{col}). Now click destination.")
                return
            # Second click: move piece
            fr, fc = self.selected
            success, msg = self.game.move_piece(fr, fc, row, col)
            self.info.config(text=msg)
            # Reset selection on success
            if success:
                self.selected = None
                self.action = None
            # Check win
            win, reason = self.game.check_win()
            if win:
                self.info.config(text=f"Game Over! {reason}")
                # disable canvas clicks
                self.canvas.unbind("<Button-1>")
            self.update_display()

        else:
            self.info.config(text="Choose 'Draw Piece' or 'Move Piece' first.")
