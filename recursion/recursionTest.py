def f(n):
    if n < 1:
        return n
    else:
        result = f(n-1)
        print(result)
        result = result + 1
        return result

print(f(5))

