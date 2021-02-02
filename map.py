from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт

import requests
from PIL import Image
from telethon.client import buttons


class Map:
    buttons = {'left': 'self.x -= 10',
               'right': 'self.x += 10',
               'up': 'self.y += 10',
               'down': 'self.y -= 10'
               }

    def __init__(self, x, y, scale):
        self.pos_x = x
        self.pos_y = y
        self.scale = scale

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

        Image.open(BytesIO(
            response.content)).show()

    def shift(self, button):
        eval(buttons[button])
        return self.get_map()


