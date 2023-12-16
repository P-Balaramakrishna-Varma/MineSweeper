import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtCore import pyqtSignal, QObject
import time
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt


class CustomButton(QPushButton):   
    def __init__(self, parent=None):
        super().__init__(parent)
        self.flagged = False
        self.revealed = False

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton and self.revealed == False:
            # Change color to red on right-click
            pal = self.palette()
            pal.setColor(QPalette.Button, QColor(Qt.red))
            self.setPalette(pal)
            self.update()
            self.flagged = True
        else:
            # Handle left-click normally
            if self.flagged == True:
                pal = self.palette()
                pal.setColor(QPalette.Button, QColor(Qt.white))
                self.setPalette(pal)
                self.update()
            super().mousePressEvent(event)


class Map(QWidget):
    def __init__(self, rows, cols, no_mines):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.no_mines = no_mines
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.grid = [[False for _ in range(cols)] for _ in range(rows)]

        self.create_and_mines()
        self.game = self.get_numbers_()

        self.setWindowTitle("Minesweeper")
        self.map_layout = QGridLayout()
        self.map_layout.setSpacing(2)
        self.map_layout.setSizeConstraint(QGridLayout.SetFixedSize)

        self.init_map()
        self.setLayout(self.map_layout)
        self.seen_count = 0
        


    def init_map(self):
        for x in range(0, self.rows):
            for y in range(0, self.cols):
                w = CustomButton()
                w.setFixedSize(30, 30)
                w.row = x
                w.col = y
                w.clicked.connect(self.trigger_start)
                self.map_layout.addWidget(w, x, y)
                self.buttons[x][y] = w

    def create_and_mines(self):
        positions = []
        while len(positions) < self.no_mines:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)
            if not self.grid[x][y]:
                self.grid[x][y] = True
                positions.append((x, y))

    def no_adjacent_mines(self, x, y):
        count = 0
        dis = [-1, 0, 1]
        for diffx in dis:
            for diffy in dis:
                X = x + diffx
                Y = y + diffy
                if (
                    X >= 0
                    and Y >= 0
                    and X < self.rows
                    and Y < self.cols
                    and self.grid[X][Y]
                ):
                    count += 1
        if self.grid[x][y]:
            count -= 1
        return count

    def get_numbers_(self):
        temp = [0 for _ in range(self.cols)]
        game = [temp.copy() for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                game[r][c] = self.no_adjacent_mines(r, c)
        return game

    def trigger_start(self):
        button = self.sender()
        if not button.revealed:
            if self.grid[button.row][button.col]:
                print("Game Over")
                exit() # smooth exits
            else:
                button.setText(str(self.game[button.row][button.col]))
                button.revealed = True
                self.seen_count += 1
                if(self.seen_count == (self.rows * self.cols) - self.no_mines):
                    print("You win!")
                    exit() # smooth exits

    # Other methods...
    def print_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                print(self.game[r][c], end=" ")
            print("")
        
        for r in range(self.rows):
            for c in range(self.cols):
                print(self.grid[r][c], end=" ")
            print("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    map = Map(2, 2, 1)
    map.show()
    map.print_grid()
    sys.exit(app.exec_())
