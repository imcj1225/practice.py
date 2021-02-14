import turtle
turtle.shape('turtle')

def maken(n):
    turtle.circle(50, steps = n)
turtle.done()

n = int(input('몇각형을 그릴까요?: '))
maken(n)
