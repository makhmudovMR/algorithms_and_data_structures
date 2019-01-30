from turtle import *

def serp(l, n, t):
    if n == 0:
        t.begin_fill()
        t.forward(l)
        t.left(120)
        t.forward(l)
        t.left(120)
        t.forward(l)
        t.left(120)
        t.end_fill()
    else:
        serp(l/2, n-1, t)
        t.forward(l/2)
        serp(l/2, n-1, t)
        t.left(120)
        t.forward(l/2)
        t.right(120)
        serp(l/2, n-1, t)
        t.right(120)
        t.forward(l/2)
        t.left(120)

rang = input('range: ')
t = Turtle()
t.speed(0)
serp(200, int(rang), t)
sc = Screen()
sc.exitonclick()
