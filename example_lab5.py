import turtle

def sierpinski(t, order, size):
    colors = ['red','blue','purple']
    if order == 0:
        for i in range(3):
            t.pencolor(colors[i])
            t.forward(size)
            t.left(120)
    else:
        sierpinski(t, order-1, size/2)
        t.forward(size/2)
        sierpinski(t, order-1, size/2)
        t.backward(size/2)
        t.left(60)
        t.forward(size/2)
        t.right(60)
        sierpinski(t, order-1, size/2)
        t.left(60)
        t.backward(size/2)
        t.right(60)

t = turtle.Turtle()
t.speed(0)
sierpinski(t, 4, 200)
turtle.done()