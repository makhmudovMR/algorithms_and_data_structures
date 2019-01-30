

def h(n, b, e):
    """
        begin tmp end
    """
    if n == 1:
        print(b, "->", e)
    else:
        tmp = 6 - b - e
        h(n-1, b, tmp)
        print(b, "->", e)
        h(n-1, tmp, e)

t(3, 1, 2)