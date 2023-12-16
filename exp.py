import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout
from PyQt5.QtCore import Qt





class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Login Form')

        # set the grid layout
        layout = QGridLayout()
        self.setLayout(layout)



        # # username
        # layout.addWidget(QLabel('Username:'), 0, 0)
        # layout.addWidget(QLineEdit(), 0, 1)

        # # password
        # layout.addWidget(QLabel('Password:'), 1, 0)
        # layout.addWidget(QLineEdit(echoMode=QLineEdit.EchoMode.Password), 1, 1)

        # # buttons
        # layout.addWidget(QPushButton('Log in'), 2, 0, alignment=Qt.AlignmentFlag.AlignRight)
        # layout.addWidget(QPushButton('Close'), 2, 1, alignment=Qt.AlignmentFlag.AlignRight)

        # # show the window
        # self.show()

  
    # to create rows * cols grid with mines randomly placed
    def create_and_mines(self): 
        postions = []
        while len(postions) < self.no_mines:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)
            if(self.grid[x][y]):
                continue
            else:
                self.grid[x][y] = True
                postions.append((x, y))
                
    def no_adjacent_mines(self, x, y):
        count = 0
        dis = [-1, 0, 1]
        for diffx in dis:
            for diffy in dis:
                X = x + diffx
                Y = y + diffy
                if(X >= 0 and Y >= 0 and X < self.rows and Y < self.cols and self.grid[X][Y]):
                    count += 1 
        if(self.grid[x][y]):
            count -= 1
        return count    

    def get_numbers_(self):
        temp = [0 for _ in range(self.cols)]
        game = [temp.copy() for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                game[r][c] = self.no_adjacent_mines(r, c)
        return game

    def print_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                print(self.game[r][c], end=" ")
            print("")
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
