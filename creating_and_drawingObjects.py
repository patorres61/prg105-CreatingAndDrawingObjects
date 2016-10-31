# Phyllis Torres
# Create and Draw Objects
# Due Date: November 3, 2016

# import swampy
from swampy.World import World

# create a world object from World class
world = World()

# define classes for point, circle, and rectangel
# noinspection PyPep8
class Point:
    """defines a point in 2 dimensional space
            """
    def __init__(self):
        pass


# noinspection PyPep8
class Circle:
    """defines a circle"""
    def __init__(self):
        pass


# noinspection PyPep8
class Rectangle:
    """defines a rectangle"""
    def __init__(self):
        pass


# define  a canvas
canvas = world.ca(width=1000, height=1000, background='linen')

# define a function to draw a rectangle
def draw_rectangle(canvas, rect):
    bbox = [[rect.x, rect.y], [rect.x1, rect.y1]]
    canvas.rectangle(bbox, outline='black', width=4, fill='white')

# define a function to draw a rectangle with a fill color
def draw_rectangle_color(canvas, rect1, color):
    bbox = [[rect1.x, rect1.y], [rect1.x1, rect1.y1]]
    canvas.rectangle(bbox, outline='black', width=4, fill=color)

# define a function to draw a point
def draw_point(canvas, x, y):
    canvas.circle([x, y], 3, outline='black', fill='black')

# this function instantiates a Circle object with the given attributes
def create_circle(x, y, radius):
    c = Circle()
    c.center = Point()
    c.center.x = x
    c.center.y = y
    c.radius = radius
    return c

# this function draws Circle circ on the canvas window with the given color
def draw_circle(window, circ, color):
    window.circle([circ.center.x, circ.center.y], circ.radius, outline='black', fill=color)

# populate the coordinates for a rectangle bounding box
rectangle = Rectangle()
rectangle.x = -450
rectangle.y = 200
rectangle.x1 = 0
rectangle.y1 = 250

rectangle1 = Rectangle()
rectangle1.x = -450
rectangle1.y = 100
rectangle1.x1 = 0
rectangle1.y1 = 150

# assign values to coordinates for a point
p1 = 0
p2 = 0

# assign values to create instances of circles
circle1 = create_circle(200, 200, 100)
circle2 = create_circle(200, 200, 75)
circle3 = create_circle(200, 200, 50)
circle4 = create_circle(200, 200, 25)
circle5 = create_circle(200, 200, 10)
circle6 = create_circle(-400, -50, 75)
circle7 = create_circle(-325, -50, 50)
circle8 = create_circle(-275, -50, 35)

# call function to draw a rectangle
# noinspection PyTypeChecker
draw_rectangle(canvas, rectangle)

# call function to draw a rectangle with color
draw_rectangle_color(canvas, rectangle1, 'blue')

# call function to draw a point
draw_point(canvas, p1, p2)

# call function to draw a circle
draw_circle(canvas, circle1, 'slate blue')
draw_circle(canvas, circle2, 'green')
draw_circle(canvas, circle3, 'cyan')
draw_circle(canvas, circle4, 'blue')
draw_circle(canvas, circle5, 'black')
draw_circle(canvas, circle6, 'yellow')
draw_circle(canvas, circle7, 'orange')
draw_circle(canvas, circle8, 'red')

canvas.create_text(400, 100, fill="darkblue", font="Calibri 20 italic bold", text="Creating and Drawing Objects - Phyllis Torres")

canvas.create_text(400, 500, fill="darkblue", font="Calibri 14 italic bold", text="Here is my point ==>")

world.mainloop()
