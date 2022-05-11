from rectangle import Rectangle
from triange import  Triange

rect = Rectangle()
trig = Triange()

rect.set_values(50,40)
rect.set_color('blue')

trig.set_values(50,40)
trig.set_color('red')

print(float(rect.area()))
print(rect.get_color())

print(float(trig.area()))
print(trig.get_color())