from paint import Engine2D, Triangle, Rectangle, Circle


paint1 = Engine2D(300, 300)
t = Circle(0, 1, 5)
paint1.canvas.add(t)
paint1.change_color('red')
triangle = Triangle(330, 80, 380, 10, 430, 80)
paint1.canvas.add(triangle)
paint1.draw()
paint1.change_color('black')
paint1.canvas.add(t)
triangle = Triangle(330, 80, 380, 10, 430, 80)
paint1.canvas.add(triangle)
rect = Rectangle(2, 4, 6, 9)
paint1.canvas.add(rect)
paint1.draw()
