import turtle
t = turtle.Turtle()

def koch(t, order, size):
  if order == 0:
    t.forward(size)
  else:
    #basically the turtle turns 85 degrees right and then the turtle turns 170 degrees left
    #and then 85 degrees right again; this ensures that the angle on the top of the #triangle (tear) is 10 degrees
    koch(t, order-1, size/3)
    t.right(85)
    koch(t, order-1, size/3)
    t.left(170)
    koch(t, order-1, size/3)
    t.right(85)
    koch(t, order-1, size/3)

t.penup()
t.goto(-150,60)
t.pendown()
t.speed(0)
t.color('black', 'light green')
t.begin_fill()
koch(t, 3, 1000)
t.end_fill()
turtle.done()
