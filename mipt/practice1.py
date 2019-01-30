import turtle
def task5():
    def rectangle(len):
        count = 4
        while count != 0:
            turtle.forward(len)
            turtle.left(90)
            count-=1
    turtle.speed(0)
    deep = 10
    length = 10
    while deep != 0:
        rectangle(length)
        turtle.right(90)
        turtle.penup()
        turtle.forward(10)
        turtle.left(90)
        turtle.backward(10)
        turtle.pendown()
        length +=20
        deep -= 1
    turtle.exitonclick()

def task6(n):
    degree = 360 // n
    
    while n != 0:
        turtle.forward(50)
        turtle.stamp()
        turtle.backward(50)
        turtle.left(degree)
        n-=1

def task7():
    pass


def task8():
    param = 10
    flag = True
    while flag:
        turtle.forward(param)
        turtle.left(90)
        param+= 10

def task9():
    corner=3
    flag = True
    length = 10
    while flag:
        tmp = corner
        degree = 360 / corner 
        while tmp != 0:
            turtle.forward(length)
            turtle.left(degree)
            tmp-=1
        
        turtle.right(45)
        turtle.forward(length)
        turtle.left(135)
        length+=20
        # TODO
        corner+=1
