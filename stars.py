import turtle
tw=turtle.Screen()
cl = ['red','yellow','orange','green','blue']
x=5
t = turtle.Turtle()
for i in range(10000000):
    t.color(cl[i % 5])
    t.forward(x)
    t.left(145)
    x=x+3
turtle.mainloop()