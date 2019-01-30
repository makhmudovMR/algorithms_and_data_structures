a = int(input())
b = int(input())


while a != 0 and b != 0:
    if a > b:
        a = a % b
    elif a < b:
        b = b % a

print(a+b)
