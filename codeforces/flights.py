n = int(input())
flights = input()

x = 0

for i in range(len(flights)-1):
    if flights[i] == 'S' and flights[i+1] == 'F':
        x+=1
    if flights[i] == 'F' and flights[i+1] == 'S':
        x-=1

if x > 0:
    print('YES')
else:
    print('NO')