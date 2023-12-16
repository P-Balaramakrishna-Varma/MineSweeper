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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
