from pythonds.basic.stack import Stack

def f(n):
    if n < 1:
        return n
    else:
        print(n)
        return f(n-1)


res = f(5)

print('result ', res)
