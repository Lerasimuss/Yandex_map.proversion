from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт

import requests
from PIL import Image


class Map:
    def __init__(self, x, y, scale):
        self.x = x
        self.y = y
        self.scale = scale
        self.get_map(self.x, self.y, self.scale)

    def get_map(self, x, y, scale):
        api_server = "http://static-maps.yandex.ru/1.x/"
        lon = str(x)
        lat = str(y)
        delta = str(scale)

        params = {
            "ll": ",".join([lon, lat]),
            "spn": ",".join([delta, delta]),
            "l": "map"
        }
        response = requests.get(api_server, params=params)

        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)

    def shift(self, button):
        if button == "up":
            return self.y + 5
        if button == "down":
            return self.y - 5
        if button == "right":
            return self.x + 5
        if button == "left":
            return self.x - 5
