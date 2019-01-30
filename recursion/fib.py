def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fib2(n):
    tmp = [0,1]
    inx = 1
    while inx < n:
        res = tmp[inx-1] + tmp[inx]
        tmp.append(res)
        inx +=1
    return tmp[len(tmp)-1]
        

def fib3(n):
    res = 0
    arr_1 = 0
    arr_curr = 1
    inx = 1
    while inx < n:
        res = arr_1 + arr_curr
        arr_1 = arr_curr
        arr_curr = res
        inx+=1
    return res


print(fib3(7))
print(fib2(7))
