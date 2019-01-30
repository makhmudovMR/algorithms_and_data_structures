import time
from random import *


mem = [0] * 100
def fib_mem(n):
    if n <= 1:
        return 1
    if mem[n] != 0:
        return mem[n]
    mem[n] = fib_mem(n-1) + fib_mem(n-2)
    return mem[n]


def fib(n):
    if n <=1 :
        return 1
    return fib(n-1) + fib(n-2)


def fib_arr(n):
    alist = [0,1] + [0] * n
    for i in range(2, len(alist)):
        alist[i] = alist[i-1]+alist[i-2]
    print(alist)

def fib_without_memory(n):
    a = 0
    b = 1
    c = 0
    i=0
    while i <= n:
        c = a + b
        a = b
        b = c
        i+=1
    return c



def grig_traj(n):
    way = [0] * (n+1)
    way[0] = 1
    way[1] = 1
    for i in range(2, len(way)):
        way[i] = way[i-3] + way[i-2] + way[i-1]
    return way[n]


def grig_traj2(n, allowed=[]):
    way = [0] * (n+1)
    way[0] = 1
    way[1] = 1
    for i in range(2, len(way)):
        if allowed[i-2]:
            way[i] = way[i-2] + way[i-1]
    return way[n]

def grig_traj3(n, price=[]):
    """
    F[n] = минимальная сумма денег
    Рассуждать о задаче с конца
    Решать с начала
    относиться к предидущим элементам/ячейкам как к уже решённым (задачам)
    """
    
    if price == []:
        return 0
    price = [0] + [randint(1, 10) for _ in range(n+1)]
    price = [0,6,2,5,2,1]
    way = [0] * (n+1)
    summ = [0] * (n+1)
    for i in range(2, len(way)):
        summ[i] = price[i] + min(summ[i-1], summ[i-2])
    return summ[-1]


def teacher_version():
    n = 5
    price = [0] + [randint(1, 10) for _ in range(n+1)]
    price = [0,6,2,5,2,1]
    prev = [-1] * (n+1)
    f = [0] * (n+1)
    f[-1] = 0
    
    for i in range(2, n+1):
        if f[i-1] > f[i-2]:
            f[i] = price[i] + f[i-2]
            prev[i] = i-2
        else:
            f[i] = price[i] + f[i-1]
            prev[i] = i-1


    print(prev)
    return f[-1]
    
    
    
"""
    1. F[n] целевая функция что мы считаем
    2. реккурентное соотношение
    3. начальные значения
    4. цикл
"""

def main():
    print(grig_traj2(5, [True for i in range(5)]))
    print(grig_traj3(5, [0,6,2,5,2,1]))
    print(teacher_version())

if __name__ == "__main__":
    main()
