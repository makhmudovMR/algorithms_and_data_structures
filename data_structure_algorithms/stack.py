from pythonds.basic import Stack

def task1():
    '''
        Проверка сбалансированности скобок в выражении
    '''
    string = '[]()(([]))'
    stack = Stack()
    flag = True
    for item in string:
        print(item)
        if item in '[({':
            stack.push(item)
        else:
            if item in '})]' and not stack.isEmpty():
                if stack.peek() == item or not stack.isEmpty():
                    stack.pop()
                else:
                    flag = False
            else:
                flag = False
    
    if not stack.isEmpty():
        flag = False
    
    print(flag)


def task2():
    '''
        Сортировка значений в стеке
        (неэффективный метод)
    '''
    import random
    random.seed(1)
    stack = Stack()
    for i in range(10):
        stack.push(random.randint(0, 9))

    tmp = []

    while not stack.isEmpty():
        tmp.append(stack.pop())
    print(tmp)

    i = 0
    while i < len(tmp):
        j=0
        while j < len(tmp)-i-1:
            if tmp[j] > tmp[j+1]:
                tmp[j], tmp[j+1] = tmp[j+1], tmp[j]
            j+=1
        i+=1

    while tmp != []:
        stack.push(tmp.pop(0))

    while not stack.isEmpty():
        print(stack.pop(), end='')



def task3():
    pass

task2()