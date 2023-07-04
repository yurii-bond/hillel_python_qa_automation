# polymorphizm
print(5)

print('Hello')

print([1, 2, 3, 4])

def convert_to_string(arg):
    return str(arg)

print(convert_to_string(5))
print(convert_to_string('Hello'))
print(convert_to_string([1, 2, 3, 4]))

print('\n')

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render(self):
        print(f'Render shape with the point: x: {self.x}, y: {self.y}')

class Circle(Shape):
    def __init__(self, x, y, radius):
        Shape.__init__(self, x, y)
        self.radius = radius

    def render(self):
        print(f'Render circle with the center in the point x: {self.x}, y: {self.y} and radius {self.radius}')

shape = Shape(5, 4)

circle = Circle(5, 4, 10)

shape.render()
circle.render()

print('\n')

class Square(Shape):
    def __init__(self, x, y, length):
        Shape.__init__(self, x, y)
        self.length = length
    def render(self):
        print(f'Render square with the beginning at the point x: {self.x}, y: {self.y} and side lenght: {self.length}')

square = Square(4, 5, 3)
square.render()

print('\n')
def render(_shape):
    if isinstance(_shape, Circle):
        print(f'Render circle with the center: x: {_shape.x}, y: {_shape.y} and radius {_shape.radius}')
    elif isinstance(_shape, Square):
        print(f'Render square with the beginning at the point x: {_shape.x}, y: {_shape.y} and side length: {_shape.length}')
    elif isinstance(_shape, Shape):
        print(f'Render shape with the point x: {_shape.x}, y: {_shape.y}')
    else:
        print(f'The argument has unsupported class: _shape is {type(_shape )}')

render(shape)
render(circle)
render(square)
render((1, 2, 3))

#print(Shape.mro())
#print(Circle.mro())

#render(shape)
print('\n')

a = 4
b = 4
#x = 'hello'
#y = 'hello'
x = Shape(4, 5)
y = Shape(4,5)

print(a == b)
print(a is b)
print(x == y)
print(x is y)

print('\n'*2)

# encapsulation
class Encaps:
    def __init__(self, a, c):
        self._a = a
        self.__b = None
        self.c = c

    def set_b(self, b):
        self.__b = b

    def get_b(self):
        return self.__b

a, b, c = 1, 2, 3

encaps = Encaps(a, c)
encaps.set_b(b)

print(encaps.c)
print(encaps._a)
print(encaps.get_b())


class NewClass(Encaps):
    def __init__(self, a, c):
        Encaps.__init__(self, a, c)

    def __str__(self):
        return str(self.c) + str(self._a)

    def set_c(self, b):
        self.__b = b

new_class = NewClass(a, c)

print(new_class)