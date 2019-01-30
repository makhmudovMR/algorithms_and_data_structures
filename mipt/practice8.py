import sys
import turtle

def fac(n, deep=0):
    if n == 1:
        print(deep)
        return 1
    return n * fac(n-1, deep+1)

def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(6))

'''
------------------
'''


def draw(l, n):
    if n == 0:
        turtle.left(180)
        return

    x = l / (n + 1)
    for i in range(n):
        turtle.forward(x)
        turtle.left(45)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        turtle.left(90)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(l)

# turtle.speed(0)
import turtle
 
turtle.shape('turtle')
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
 
def Koch_Line (l ,n):
    if n == 0:
        turtle.forward(l)
        return
    l //= 3
    Koch_Line(l, n-1)
    turtle.left(60)
    Koch_Line(l, n-1)
    turtle.right(120)
    Koch_Line(l, n-1)
    turtle.left(60)
    Koch_Line(l, n-1)
   
  
Koch_Line(400, 4)