import turtle
import colorsys
s=turtle.Turtle()
turtle.bgcolor("white")
h=1.0
s.speed(0)
for i in range(200):
    s.color(colorsys.hsv_to_rgb(h,1,1))
    for j in range(8):
        s.forward(i)
        s.right(120)
    s.right(8)
    h+=0.02 
turtle.mainloop()
