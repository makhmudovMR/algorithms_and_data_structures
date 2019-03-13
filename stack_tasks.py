from pythonds import Stack
from random import randint
import random

'''
    Wrong
'''
def task1():
    random.seed(1)
    '''сортировка стека'''
    stack1 = Stack()
    stack2 = Stack()
    stack3 = Stack()
    buff = None

    
    for _ in range(10):
        stack1.push(randint(0, 9))

    
    
    while not stack1.isEmpty():
        if stack2.isEmpty():
            stack2.push(stack1.pop())
        else:
            print(buff)
            buff = stack1.pop()
            if stack2.peek() > buff:
                flag = True
                while flag:
                    if stack2.isEmpty() or stack2.peek() < buff:
                        break
                    stack3.push(stack2.pop())

                stack2.push(buff)

                while not stack3.isEmpty():
                    stack2.push(stack3.pop())

    
    # print
    while not stack2.isEmpty():
        print(stack2.pop(), end=' ')
    
    

task1()