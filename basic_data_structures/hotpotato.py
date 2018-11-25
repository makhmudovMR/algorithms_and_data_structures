from pythonds.basic.queue import Queue


def game(q, num):
    iter = 0
    while q.size() != 1:
        tmp = q.dequeue()
        print(tmp)
        if iter != num:
            q.enqueue(tmp)
        else:
            iter = 0
        iter += 1
    return q.dequeue()


q = Queue()
q.enqueue('Bill')
q.enqueue('Jhon')
q.enqueue('Frank')
q.enqueue('Ivan')
q.enqueue('Fun')

print('Победитель', game(q, 2))

'''
book example

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
'''