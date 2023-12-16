# Game Play
## Starting the Game
- Conda environment file is provided to install the requirements.
- Run minesweeper.py
- One can change the dimensions of the board and the number of mines by changing line ```map = Map(5, 5, 1)``` to
```map = Map(rows, cols, mines)```

## Left Click
- Left click on a box to reveal it.
    - If the box turns out to be a mine, you lose.
    - Otherwise, the box will show a number indicating the number of mines in the adjacent boxes.

## Right Click
- A user can right click on a box to flag if they suspect it to be a mine.

## Game Loop
- The game ends when the user has revealed all the boxes that are not mines. The GUI window title changes to "You won".
- The game ends when the user has revealed a mine. The GUI window title changes to "You lost".
- User keeps on revealing boxes until they win or lose.


