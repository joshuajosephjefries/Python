import turtle
bob=turtle.Turtle()

def petal(t, r, angle):
    for i in range(2):
        bob.circle(r, angle)
        bob.lt(180-angle)

def flower(t, r, n, angle):
    for i in range(n):
        petal(t,r,angle)
        t.lt(360/n)

bob.speed(100)

bob.penup()
bob.bk(200)
bob.pendown()

flower(bob,80,7,80)

bob.penup()
bob.fd(200)
bob.pendown()

flower(bob,80,10,80)

bob.penup()
bob.fd(200)
bob.pendown()

flower(bob,150,20,30)

turtle.done()
