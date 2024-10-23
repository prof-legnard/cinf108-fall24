import turtle
t = turtle.Turtle()
t.speed(0)
color_size = [('red',50), ('blue', 100), ('green',150)]


i = 1

while i <= 8:
    for color, size in color_size[::-1]:
        t.pencolor(color)
        t.fillcolor(color)
        t.begin_fill()
        t.forward(25)
        t.circle(size)
        t.end_fill()
    t.right(60)
    i+=1
t.penup()
t.home()
t.pendown()
t.pencolor('black')
t.fillcolor('black')
t.begin_fill()
t.right(120)
for _ in range(6): 
  t.forward(75) 
  t.right(-60) 
t.end_fill()

turtle.done()
