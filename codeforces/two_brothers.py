a, b = list(map(int, input().split()))

i = 0

while True:
    a*=3
    b*=2
    i+=1
    if a>b:
        break



print(i)