def f(alist):
    print(alist)
    if len(alist) <= 1:
        return alist
    else:
        return f(alist[1:])


alist = [i for i in range(10)]
f(alist)