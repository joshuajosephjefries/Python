import turtle
bob=turtle.Turtle()

def petal(t, r, angle):
    for i in range(2):
        bob.circle(r,angle)
        bob.lt(180-angle)
def flower(t,r,n,angle):
    bob.color('red', '#9400D3')
    bob.begin_fill()
    petal(t,r,angle)
    t.lt(360/n)
    bob.end_fill()

    bob.color('red', '#4B0082')
    bob.begin_fill()
    petal(t, r, angle)
    t.lt(360 / n)
    bob.end_fill()

    bob.color('red', '#0000FF')
    bob.begin_fill()
    petal(t, r, angle)
    t.lt(360 / n)
    bob.end_fill()

    bob.color('red', '#00FF00')
    bob.begin_fill()
    petal(t, r, angle)
    t.lt(360 / n)
    bob.end_fill()

    bob.color('red', '#FFFF00')
    bob.begin_fill()
    petal(t, r, angle)
    t.lt(360 / n)
    bob.end_fill()

    bob.color('red', '#FF7F00')
    bob.begin_fill()
    petal(t, r, angle)
    t.lt(360 / n)
    bob.end_fill()

    bob.color('red', '#FF0000')
    bob.begin_fill()
    petal(t, r, angle)
    t.lt(360 / n)
    bob.end_fill()

bob.speed(100)

flower(bob, 80, 7, 80)

bob.pu()
bob.fd(200)
bob.pd()

flower(bob, 80, 7, 80)

bob.pu()
bob.bk(400)
bob.pd()

flower(bob, 80, 7, 80)
turtle.done()
