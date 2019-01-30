'''
    Сумма чисел через рекурсию 
'''



def sum(a, b):
    if b == 0:
        return  a
    else:
        return sum(a, b-1) + 1

def sum2(a, b):
    if a == 0:
        return b
    else:
        return sum(a-1, b+1)


def sumN(n):
    if n == 0 :
        return n
    else:
        return sumN(n-1) + n


'''
сумма всех цифр 
'''
def sDigits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sDigits(n//10)


def check(n):
    if n == 1:
        return True
    else:
        return (n % 2 == 0) and check(n // 2)


def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])



'''
123 -> 1 2 3
'''

def p(n):
    if n < 10:
        print(n, end = ' ')
    else:
        p(n//10)
        print(n % 10, end = ' ')


'''
a*b
'''
def pow(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    else:
        return pow(a, n-1) * a


def pow2(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    else:
        if n % 2 == 0:
            return pow(a, n//2) ** 2
        else:
            return pow(a, n-1) * a

def matr(n):
    if n == 1:
        print('Матрёшка ', n)
    else:
        print('Верх матрёшки n=',n)
        matr(n-1)
        print('Низ матрёшки n=', n)

matr(5)



    

