import sys
from map_interface import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from map import Map
from scale import Scale


class Map_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.x = int(input())
        if self.x > 175:
            self.x = 175
        elif self.x < -175:
            self.x = -175
        self.y = int(input())
        if self.y > 80:
            self.y = 80
        elif self.y < -80:
            self.y = -80
        self.sc = Scale()
        self.spn = self.sc.get_scale()
        self.map_show()

    def map_show(self):
        Map(self.x, self.y, self.spn)
        pixmap = QPixmap("map.png")
        self.map_window.setPixmap(pixmap)
        self.lcd_x.display(self.x)
        self.lcd_y.display(self.y)
        self.lcd_scale.display(self.spn)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.y = Map(self.x, self.y, self.spn).shift("up")
        if event.key() == Qt.Key_Down:
            self.y = Map(self.x, self.y, self.spn).shift("down")
        if event.key() == Qt.Key_Right:
            self.x = Map(self.x, self.y, self.spn).shift("right")
        if event.key() == Qt.Key_Left:
            self.x = Map(self.x, self.y, self.spn).shift("left")
        if event.key() == Qt.Key_PageUp:
            self.spn = self.sc.scale_down()
        if event.key() == Qt.Key_PageDown:
            self.spn = self.sc.scale_up()
        self.map_show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Map_window()
    ex.show()
    sys.exit(app.exec())
