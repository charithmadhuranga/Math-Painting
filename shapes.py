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
