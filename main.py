import numpy as np
from PIL import Image


class Sqaure:

    def __init__(self, side, color, x, y):
        self.side = side
        self.color = color
        self.x = x
        self.y = y

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle:

    def __init__(self, width, height, color, x, y):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color



"""creating the canvas with user specified width and height and color"""
class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        #create 3d zeros numpy array
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        #fill the [0,0,0] np array with user given color
        self.data[:] = self.color
    #convert current array into and image
    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)

canvas = Canvas(20, 30, (255, 255, 255))
square = Sqaure(3, (0,100,222), 1, 3)
square.draw(canvas)
rectangle = Rectangle(7, 10, (100, 200, 125), 1, 6)
rectangle.draw(canvas)
canvas.make('canvas.png')