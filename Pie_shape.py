import math
import turtle
bob=turtle.Turtle()
def draw_shape(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, length, angle/2)
        t.lt(angle)
    t.pu()
    t.fd(100)
    t.pd()
def isosceles(t, length, angle):
    y = length * math.sin(angle * math.pi / 180)
    t.rt(angle)
    t.fd(length)
    t.lt(90 + angle)
    t.fd(2 * y)
    t.lt(90 + angle)
    t.fd(length)
    t.lt(180 - angle)
draw_shape(bob, 5, 40)
draw_shape(bob, 6, 40)
draw_shape(bob, 7, 40)
turtle.done()
