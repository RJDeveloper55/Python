class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color
        # print(speed)
        # print(color)
        # print('__init__ is called')

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color

ford = Car(200, 'red')
#print(ford.__speed)
ford.set_speed(400)
print(ford.get_speed())
ford.set_color('green')
print(ford.get_color())

# ford.Color = 'red'
# ford.Speed = '250'

#honda = Car(250, 'blue')
# honda.Color = 'blue'
# honda.Speed = '220'

#isuzu = Car(280, 'white')
#isuzu.Color = 'white'
#isuzu.Speed = '240'
#print(isuzu.Color)
#print(isuzu.Speed)

# ford.Color = 'black'
# isuzu.Code = 'gray'

# print(ford.Color)
# print(isuzu.Color)

