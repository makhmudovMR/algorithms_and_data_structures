def bin(n):
    if n <= 1:
        return n
    else:
        return bin(n//2)

print(bin(4))