def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n-1)

def f2(n):
    sum = 1
    for i in range(1,n+1):
        sum *=i
    return sum

print(f(3))
print(f2(3))