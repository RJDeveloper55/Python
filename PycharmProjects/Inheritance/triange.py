from polygon import Polygon
from shape import Shape


class Triange(Polygon, Shape):
    def area(self):
        return self.get_heigth() * self.get_width() / 2