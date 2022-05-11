class Rectangle:
    def __init__(self, height, width):
        self.__height=height
        self.__width= width

    def set_height(self, value):
        self.__height = value

    def get_height(self):
        return self.__height

    def set_width(self, value):
        self.__width = value

    def get_width(self):
        return self.__width

    def calculate_area(self):
        return self.__height * self.__width

rect1=Rectangle(200, 250)
rect2=Rectangle(250, 180)

# rect1.height = 200
# rect2.height = 350
#
# rect1.width = 180
# rect2.width = 280

# rect1Area = rect1.height * rect1.width
# rect2Area = rect2.height * rect2.width

# print('Rectangle1 Area = ', rect1Area)
# print('Rectangle2 Area = ', rect2Area)

print('Rectangle1 Area = ', rect1.calculate_area())
print('Rectangle2 Area = ', rect2.calculate_area())
