import requests


class Scale:
    def __init__(self, scale=10):
        self.scale = scale

    def get_scale(self):
        return self.scale

    def set_scale(self, scale):
        self.scale = scale

    def scale_up(self, scale=0.1):
        if 0 <= self.scale + scale <= 180:
            self.scale += scale

    def scale_down(self, scale=0.1):
        if 0 <= self.scale - scale <= 180:
            self.scale -= scale

    def get_image(self, ll, level='map'):
        map_server = "http://static-maps.yandex.ru/1.x/"
        map_params = {
            "ll": ",".join(map(str, ll)),
            "spn": ",".join(map(str, (self.scale, self.scale))),
            "l": level}
        return requests.get(map_server, params=map_params).content

# тест
# ------------------------------
# from io import BytesIO
# from PIL import Image
# sc = Scale()
# # sc.scale_down(3)
# # sc.scale_down(5)
# a, b = str(sc.get_scale()), str(sc.get_scale())
# Image.open(BytesIO(sc.get_image((37.530887, 55.703118)))).show()
