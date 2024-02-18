# Circles in colors

import turtle

colors = ["red", "blue", "purple", "orange", "yellow", "green"]

t = turtle.Turtle()
t.pencolor("black")
t.fillcolor("orange")
# turtle.bgcolor("blue")
t.pensize(2)
t.speed(10)

for i in range(10):
  t.pencolor(colors[i % len(colors)])
  t.circle(20*(10-i))
  t.penup()
  t.left(90)
  t.forward(20)
  t.right(90)
  t.pendown()

turtle.mainloop()
