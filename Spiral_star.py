import turtle
bob=turtle.Turtle()
turtle.bgcolor('cyan')
bob.color('red', 'light green')
bob.pensize(3)
bob.begin_fill()
bob.speed(10)

for i in range(80):
    bob.fd(300)
    bob.lt(150)

bob.end_fill()
turtle.done()
