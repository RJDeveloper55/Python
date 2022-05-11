from abc import ABC, abstractmethod


class Shape(ABC):
    __color = None

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color


    @abstractmethod
    def area(self): pass
    @abstractmethod
    def parimeter(self): pass


class Square(Shape):
    def __init__(self, side):
        self.__side = side
    def area(self):
        return self.__side * self.__side
    def parimeter(self):
        return 4 * self.__side


square = Square(5)
print(square.area())
print(square.parimeter())
