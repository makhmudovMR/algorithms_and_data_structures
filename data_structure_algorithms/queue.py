from pythonds.basic import Queue

def task1():
    '''
        Реализация стека с помощью очереди.
    '''
    queue1 = Queue()
    queue2 = Queue()

    def push(item):
        queue1.enqueue(item)

    def pop():
        if queue1.size() > 1:
            while queue1.size() - 1 != 0:
                queue2.enqueue(queue1.dequeue())
            tmp = queue1.dequeue()
            while queue2.size() != 0:
                queue1.enqueue(queue2.dequeue())
            return tmp
        else:
            return queue1.dequeue()

    push(1)
    push(2)
    push(3)
    push(4)
    for _ in range(4):
        print(pop())


def task2():
    'Развернуть первые k элементов.'
    k = 5
    inputs = [i for i in range(10)]
    queue1 = Queue()
    queue2 = Queue()
    for item in inputs:
        queue1.enqueue(item)
    
    while (queue1.size() - k) != 0:
        queue2.enqueue(queue1.dequeue())
    
    tmp = []
    while queue1.size() != 0:
        tmp.append(queue1.dequeue())
    
    while queue2.size() != 0:
        queue1.enqueue(queue2.dequeue())
    
    while tmp != []:
        queue1.enqueue(tmp.pop())
    
    while queue1.size() != 0:
        print(queue1.dequeue(), end='')


def task3():
    '''Генерация двоичных чисел от 1 до n с помощью очереди'''
    n = 5
    queue = Queue()
    i = 0
    while i < n:
        pass

task2()
