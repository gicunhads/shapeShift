# ☁️ Shapeshift

🩶 A strategic board game inspired by Quarto and Chess.  :)

Align pieces by shape, size, or color—and stay one step ahead of your opponent!

The draw pool order is unpredictable—your opponent can be given the exact piece you need.

Piece-movement adds a second layer: any piece can be shifted, blocking or creating new lines.

---

## ✼ Overview

Shapeshift is played on a 5×5 grid with exactly eight unique pieces.  
Each piece has three attributes:
- **Color:** Black or White  
- **Shape:** Heart or Square  
- **Size:** Big or Small  

Players take turns **drawing** a random piece from the pool and **placing** it, or **moving** any piece on the board. Your goal is to form a line of **four** pieces sharing one attribute (shape, size, or color) in a row, column, or diagonal.

---

## △ Installation & Run

1. Clone the repo:  
   ```bash
   git clone https://github.com/yourusername/shapeshift.git
   cd shapeshift
    ```

Launch the GUI:
  ```bash
python gui.py
```
---
## → Game Rules

All eight pieces start in a shuffled draw‐pool.

The 5×5 board is empty.

Draw & Place: Draw the top piece from the pool, then place it on any empty cell.

Move Piece: Select any piece on the board, then move it according to its movement rules.
---

## Movement Rules

Hearts (♥︎🖤/♡🤍) move diagonally.

Squares (⬛️/⬜️/▪️/▫️) move orthogonally (up, down, left, right).

Big pieces move up to 3 cells; Small pieces move exactly 1 cell.

Pieces cannot jump over occupied cells.

---
## → Win Conditions
You win instantly when four pieces that share one attribute form a straight line (horizontal, vertical, or diagonal):

Shape Win: four Hearts or four Squares in line

Size Win: four Bigs or four Smalls in line

Color Win: four Blacks or four Whites in line

