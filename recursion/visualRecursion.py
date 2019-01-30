import turtle

def sipr(dis, t):
    if dis > 0 :
        t.forward(dis)
        t.left(45)
        t.forward(dis * 0.5)
        t.backward(dis * 0.5)
        t.right(135)
        sipr(dis - 5, t)
        t.left(90)
        t.backward(dis)

def tree(branch, t):
    if branch > 0:
        if branch <= 10:
            t.color('green')
        else:
            t.color('black')
        t.forward(branch)
        t.right(20)
        t.pensize(t.pensize() * 0.5)
        tree(branch - 10, t)
        t.left(40)
        tree(branch - 10, t)
        t.right(20)
        t.backward(branch)


t = turtle.Turtle()
t.left(90)
t.pensize(5)
win = turtle.Screen()
tree(50, t)
win.exitonclick()

