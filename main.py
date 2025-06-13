from game import Game

def main():
    game = Game()
    print("Welcome to Align & Move!")

    # Simple loop for demonstration (no input validation here)
    while True:
        game.print_board()
        if game.phase == 1:
            print("Phase 1: Draw and place a piece.")
            row = int(input("Enter row to place (0-4): "))
            col = int(input("Enter col to place (0-4): "))
            success, msg = game.place_piece(row, col)
            print(msg)
        else:
            print("Phase 2: Move a piece.")
            fr = int(input("From row: "))
            fc = int(input("From col: "))
            tr = int(input("To row: "))
            tc = int(input("To col: "))
            success, msg = game.move_piece(fr, fc, tr, tc)
            print(msg)

        win, reason = game.check_win()
        if win:
            game.print_board()
            print(f"Game Over! {reason}")
            break

if __name__ == "__main__":
    main()
