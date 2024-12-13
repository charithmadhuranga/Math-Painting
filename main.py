from canvas import Canvas
from shapes import Sqaure, Rectangle

canvas = Canvas(20, 30, (255, 255, 255))
square = Sqaure(3, (0, 100, 222), 1, 3)
square.draw(canvas)
rectangle = Rectangle(7, 10, (100, 200, 125), 1, 6)
rectangle.draw(canvas)
canvas.make('canvas.png')