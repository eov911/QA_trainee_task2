from tkinter import *


class Circle():
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
    
    def draw(self, canvas):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill=self.color, outline=self.color) 


class Triangle():
    def __init__(self, x1, y1, x2, y2, x3, y3, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.color = color

    def draw(self, canvas):
        canvas.create_polygon(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, outline=self.color, fill=self.color)


class Rectangle():
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
    
    def draw(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill = self.color, outline = self.color)


class Engine2D():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.canvas = Canvas(self.root, width=width, height=height, bg='white')
        self.canvas.pack()
        self.text = Text(width=30, height=4)
        self.text.pack()
        self.text.insert(1.0, 'You can draw:\ncircle\ntriangle\nrectangle')


    def draw(self):
        triangle.draw(painter.canvas)
        rectangle.draw(painter.canvas)
        circle.draw(painter.canvas)
        self.root.mainloop()


painter = Engine2D(500, 500)
triangle = Triangle(330, 80, 380, 10, 430, 80, '#f23233')

rectangle = Rectangle(180, 10, 280, 80, 'lightgreen')

circle = Circle(20, 90, 90, 20, 'orange')

painter.draw()
