import os
import sys
from map_interface import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
import map


class Map_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Map_window()
    ex.show()
    sys.exit(app.exec())
