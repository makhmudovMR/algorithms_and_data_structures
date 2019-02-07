'''
    Превышено ограничение времени на тесте 3
'''
n = int(input())
x = [100, 20, 10, 5, 1]
count = 0
i = 0
while n > 0:
    while n - x[i] < 0:
        i+=1
    n -= x[i]
    count+=1

print(count)