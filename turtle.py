import turtle as t

t.shape ('turtle')
t.speed(6)

t.penup()
t.backward(500)
t.pendown()


t.bgcolor('black')
t.color('green')

for i in range(3):
    t.forward(30)
    t.right(80)
    t.forward(40)
    t.left(160)
    t.forward(100)
    t.right(160)
    t.forward(150)
    t.left(160)
    t.forward(110)
    t.right(160)
    t.forward(20)
    t.left(80)
    t.forward(50)

t.speed(1)
t. forward(700)

t.done()
