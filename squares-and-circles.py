# Loop of squares and circles inside one another

import turtle
import math

tw = turtle.Screen()
color="orange"
ella = turtle.Turtle()
ella.penup()
ella.right(90)
ella.forward(490)
ella.right(90)
ella.forward(500)
ella.left(180)
ella.pendown()
ella.pensize(2)

b=980

for i in range(1000):
    ella.color(color)
    for q in range (4):
        ella.forward(b)
        ella.left(90)
    ella.forward(b/2)
    ella.circle(b/2)
    ella.left(45)
    b=b/math.sqrt(2)

    if color=="orange":
        color="red"
    else:
        color="orange"

    if b<20:
        break
turtle.mainloop()
