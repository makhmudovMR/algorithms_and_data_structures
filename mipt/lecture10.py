"""
    Бинарный поиск
"""

# разобрать

def left_bound(A, key):
    left = -1
    right = len(A)

    while right-left>1:
        mid = (left+right)// 2
        if A[mid] < key:
            left = mid
        else:
            right = mid
    return left


def right_bound(A, key):
    left = -1
    right = len(A)

    while right-left>1:
        mid = (left+right)// 2
        if A[mid] <= key:
            left = mid
        else:
            right = mid
    return right


x = [i for i in range(10)]
# print(left_bound(x, 5))
# print(right_bound(x, 5))


"""
    +-------------------------------+
    | Динамическое программирование |
    +-------------------------------+
"""


def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

def my_fib(n):
    a = 0
    b = 1
    c = None
    for i in range(n):
        c = a + b
        tmp = b
        b = c
        a = tmp
    return c

def fib_loop(n):
    fib = [1, 1] + [0] * (n - 1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[-1]

result="""
    fib_recursion:      {rec}
    fib_my:             {my}
    fib_loop_teacher:   {teach}
""".format(rec=fib(5), my=my_fib(5), teach=fib_loop(5))



def f1(n, prefix=""):
    if n == 0:
        print(prefix)
    else:
        f1(n-1, prefix+"0")
        f1(n-1, prefix+"1")


def grig(n):
    way = [0,1] + [0] * n
    for i in range(2, n+1):
        way[i] = way[i-2] + way[i-1]
    return way[n]

"""
    fib with memory

n = 25
memory = [0 for i in range(n+1)]

def fib_mem(n, memory):
    if n <= 1:
        return 1
    if memory[n] != 0:
        print('in memory')
        return memory[n]
    memory[n] = fib_mem(n-1, memory) + fib_mem(n-2, memory)
    return memory[n]

print(fib_mem(n, memory))

"""

def grig_traj(n, allowed=None):
    way = [0,1, int(allowed[2])] + [0] * (n-3)
    
    for i in range(3, n+1):
        if allowed[i]:
            way[i] = way[i-1] + way[i-2] + way[i-3]
        
    return way[-1]

"""
    Двумерный массив
"""

A = [[0] * 5 for i in range(5)]

A[0][0]+=1
print(A)

