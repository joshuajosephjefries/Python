import turtle
bob=turtle.Turtle()
turtle.bgcolor('cyan')
bob.color('red', 'light green')
bob.pensize(3)
bob.begin_fill()

def polygon(t, length, n):
    for i in range(n):
        bob.fd(length)
        bob.lt(360/n)

polygon(bob, 100, 5)

bob.end_fill()
turtle.done()
