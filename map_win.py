import os
import sys
from map_interface import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
import pygame
import requests


spn = 1
pose_x = 35
pose_y = 30
map_request = f"http://static-maps.yandex.ru/1.x/?ll={pose_x},{pose_y}&spn={spn},0.002&l=map"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)


class Map(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Map()
    ex.show()
    sys.exit(app.exec())
