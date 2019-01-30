def matryoshka(n):
    if n == 1:
        print('Матрёшка')
    else:
        print('Верх матрёшки n=',n)
        matryoshka(n-1)
        print('Низ матрёшки n=',n)

def f(n):
    if n <= 1:
        return 1
    return n * f(n-1)

def gcd(a,b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    elif a < b:
        return gcd(a, b-a)

print(gcd(40, 16))