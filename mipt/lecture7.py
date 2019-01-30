

def matr(n):
    """
        n = вложенность матрёшки
    """
    if n == 1:
        print('Матрёшка')
    else:
        print('Верх матрёшки n=', n)
        matr(n-1)
        print('Низ матрёшки n=', n)

def graph():

    import graphics as gr
    window = gr.GraphWin('Win', 600, 600)

    def farctal_rectangle(A,B,C,D, deep=10):
        alpha = 0.5
        if deep < 1:
            return
        for i, j in [(A, B), (B, C), (C, D), (D, A)]:
            gr.Line(gr.Point(*i), gr.Point(*j)).draw(window)
        A1 = (A[0] * (1-alpha) + B[0]*alpha, A[1] * (1-alpha) + B[1]*alpha)
        B1 = (B[0] * (1-alpha) + C[0]*alpha, B[1] * (1-alpha) + C[1]*alpha)
        C1 = (C[0] * (1-alpha) + D[0]*alpha, C[1] * (1-alpha) + D[1]*alpha)
        D1 = (D[0] * (1-alpha) + A[0]*alpha, D[1] * (1-alpha) + A[1]*alpha)
        farctal_rectangle(A1, B1, C1, D1, deep-1)

    farctal_rectangle((100, 100), (500, 100), (500, 500), (100, 500), 10)

    window.getMouse()

    window.close()

def fact(n):
    assert n >= 0, "error"
    if n == 1:
        return 1
    return  n * fact(n-1)



# алгоритм Евклида

def evkl():
    a = 50
    b = 130
    
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    print (a)

def evkl_recursion(a, b):
    print(a, b)
    if a == b:
        return a
    if a > b:
        return evkl_recursion(a-b, b)
    else: # a < b
        return evkl_recursion(a, b-a)

def pow(a, n):
    if n == 0:
        return 1
    return pow(a,n-1) * a if a > 0 else 0

def pow_(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return pow(a, n - 1) * a
    else:
        return pow(a**2, n//2)


print(pow(5, 4))
print(pow_(5, 4))