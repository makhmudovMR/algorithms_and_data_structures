def copy_array():
    n = int(input())
    a = [0] * n
    b = [0] * n

    for k in range(n):
        a[k] = k

    for k in range(n):
        b[k] = a[k]

    
'''
    Algorithms
'''

def array_search(A, N, x):
    """
        Осущществляет поиск числа x в A 
        от 0 до N

        Возвращает индекс элемента 
    """
    index = 0

    while index <= N:
        if A[index] == x:
            return index
        index += 1
    return -1 


def inverse_array(a):
    tmp = [0] * len(a)
    count = 0
    print(len(a))
    for i in range(len(a)-1, -1, -1):
        print(i)
        tmp[count] = a[i]
        count+=1
    return tmp

def inverse_array2(A, N):
    for k in range(N//2):
        A[k], A[N-1-k] = A[N-1-k], A[k]
    return A

def shift():
    '''
        Сдвиг влево
    '''
    A = [i for i in range(5)]
    print(A)
    i = 0
    tmp = A[0]
    while i < len(A)-1:
        A[i] = A[i+1]
        i+=1
    A[-1] = tmp
    print(A)


def shift2():
    '''
        Сдвиг вправо
    '''
    A = [i for i in range(5)]
    print(A)
    tmp = A[-1]
    for k in range(len(A)-2, -1, -1):
        A[k+1] = A[k]
    A[0] = tmp
    print(A)

def sieve(n):
    A = [True] * n
    A[0] = A[1] = False
    
    for k in range(2, n):
        if A[k]:
            for m in range(2 * k , n, k):
                A[m] = False

    print(A)
                


sieve(30)
