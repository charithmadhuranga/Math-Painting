from symtable import Class


class Sqaure:
    def __init__(self,side,color,x,y):
        self.side = side
        self.color = color
        self.x = x
        self.y = y
    def draw(self,canvas):
        pass

class Rectangle:
    def __init__(self,width,height,color,x,y):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y

    def draw(self,canvas):
        pass

class Canvas:
    def __init__(self,width,height,color):
        self.width = width
        self.height = height
        self.color = color
    def make(self,imagepath):
        pass


