import turtle
turtle.shape('turtle')

def circle(r):
    turtle.circle(r)

def triangle(l):
    for i in range(3):
        turtle.forward(l)
        turtle.right(120)

def square(l):
    turtle.left(90)
    for i in range(4):
        turtle.forward(l)
        turtle.right(90)

def hexagon(l):
    turtle.left(90)
    for i in range(6):
        turtle.forward(l)
        turtle.right(60)


