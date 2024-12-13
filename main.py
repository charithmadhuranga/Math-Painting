from canvas import Canvas
from shapes import Sqaure, Rectangle

print("*******Welcome to Math Painting*******")
canvas_width = int(input('Enter canvas width: '))
canvas_height = int(input('Enter canvas height: '))
canvas_color = input('Enter canvas color: black or white:')
colors = {'black': (0, 0, 0), 'white': (255, 255, 255)}

canvas = Canvas(canvas_width, canvas_height, colors[canvas_color])
while True:
    shape_type = input('Enter shape type: square or rectangle or exit: ')
    if shape_type.lower() == 'square':

        side = int(input('Enter square side: '))
        x = int(input('Enter x coordinate: '))
        y = int(input('Enter y coordinate: '))
        red = int(input('Enter red value: '))
        green = int(input('Enter green value: '))
        blue = int(input('Enter blue value: '))

        square = Sqaure(side, (red, green, blue), x, y)
        square.draw(canvas)

    elif shape_type.lower() == 'rectangle':

        width = int(input('Enter rectangle width: '))
        height = int(input('Enter rectangle height: '))
        x = int(input('Enter x coordinate: '))
        y = int(input('Enter y coordinate: '))
        red = int(input('Enter red value: '))
        green = int(input('Enter green value: '))
        blue = int(input('Enter blue value: '))

        rectangle = Rectangle(width, height, (red, green, blue), x, y)
        rectangle.draw(canvas)

    elif shape_type.lower() == 'exit':
        break

# square = Sqaure(3, (0, 100, 222), 1, 3)
# square.draw(canvas)
# rectangle = Rectangle(7, 10, (100, 200, 125), 1, 6)
# rectangle.draw(canvas)
canvas.make('canvas.png')