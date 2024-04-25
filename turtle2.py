import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange']
t = turtle.Pen()
turtle.bgcolor('white')
for x in range(360):
    t.pencolor(colors[x%5])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)
