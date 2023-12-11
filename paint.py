class Circle:
    def __init__(self, x1, y1, r):
        self.x1 = x1
        self.y1 = y1
        self.r = r
        self.color = painter.color

    def draw(self):
        print(f'Drawing circle. Color: {self.color}')


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.color = painter.color

    def draw(self):
        print(f'Drawing triangle. Color: {self.color}')


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = painter.color

    def draw(self):
        print(f'Drawing rectangle. Color: {self.color}')


class Canvas:
    canvas_list = []

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def add(self, element):
        self.canvas_list.append(element)

    def draw(self):
        for el in self.canvas_list:
            el.draw()

    def clean(self):
        self.canvas_list = []


class Engine2D:
    def __init__(self, width, height, color='black'):
        self.canvas = Canvas(width, height)
        self.color = color

    def draw(self):
        self.canvas.draw()
        self.canvas.clean()

    def change_color(self, color):
        self.color = color


painter = Engine2D(300, 300)
triangle = Triangle(330, 80, 380, 10, 430, 80)
painter.canvas.add(triangle)
rectangle = Rectangle(180, 10, 280, 80)
painter.canvas.add(rectangle)
circle = Circle(20, 90, 20)
painter.canvas.add(circle)
circle2 = Circle(100, 200, 100)
painter.canvas.add(circle2)
painter.draw()
painter.change_color('red')
circle3 = Circle(100, 200, 100)
painter.canvas.add(circle3)
triangle4 = Triangle(330, 80, 380, 10, 430, 80)
painter.canvas.add(triangle4)
painter.draw()
