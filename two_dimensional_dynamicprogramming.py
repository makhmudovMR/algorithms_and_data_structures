"""
    Двумерное динамическое программирование
"""

def task1():
    n, k = map(int, input().split())
    print(n, k)
    F = [0] * (n+1)
    F[0] = 1
    for i in range(1,n+1):
        F[i] = sum(F[max(0, i-k):i])
    print(F)

def task2():
    #n = int(input("Input: n"))
    n=10
    F = [0] * (n+1)
    for i in range(2, n+1):
        F[i] = F[i-1]
        if i % 2 == 0 and F[i // 2] < F[i]:
            F[i] = F[i//2]
        if i % 3 == 0 and F[i // 3] < F[i]:
            F[i] = F[i // 3]
        F[i] += 1
    print(F)
    # Востановление ответа
    ans = []
    curr = n #начинаем с конца. (мы могли прийти с F[curr-1], F[curr // 2], F[curr // 3])
    while curr > 1:
        if F[curr - i] + 1 == F[curr]:
            prev = curr - 1
        elif curr % 2 == 0 and F[curr // 2] + 1 == F[curr]:
            prev = curr // 2
        else:
            prev = curr // 3
        ans.append(curr)
        curr = prev
    ans.append(1)
    print(ans)


def task3():
    n, m = map(int, input().split())
    F = [[1 for j in range(m)] for i in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            F[i][j] = F[i-1][j] + F[i][j-1]
    
    for i in F:
        print(i)

    F = [1] * m
    for i in range(1,n):
        for j in range(1, m):
            F[j] = F[j] + F[j-1]
    print(F)

def task3v2():
    n, m = map(int, input().split())
    F = [[0 for j in range(m+1)] for i in range(n+1)]
    F[0][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            F[i][j] = F[i-1][j] + F[i][j-1]
    print(F)

def task4(n,m,x = []):
    F = [[0 for j in range(m+1)] for i in range(n+1)]
    F[0][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i][j]:
                F[i][j] = F[i-1][j] + F[i][j-1]
            else:
                F[i][j] = 0

    for i in F:
        print(i)
    for j in x:
        print(j)

def task5():
    price = [[0,0,0,0,0,0],[0,1,3,5,0,3], [0,0,1,2,4,1],[0,2,4,3,3,2],[0,3,1,2,4,3]]
    F = [[0 for j in range(len(price[0]))] for i in range(len(price))]
    for item in price:
        print(item)
    print("-----")
    for item in F:
        print(item)

    for i in range(len(price)):
        for j in range(len(price[0])):
            F[i][j] = max(F[i-1][j], F[i][j-1]) + price[i][j]
            
    print("-----")
    for item in F:
        print(item)
    i = len(F)-1
    j = len(F[0])-1
    
    ways = []
    ways.append((i,j))
    while i != 1 and j!=1:
        if F[i-1][j] > F[i][j-1]:
            i-=1
        else:
            j-=1
        ways.append((i,j))
    print(ways)
    

def main():
    #task1()
    #task2()
    #task3()
    #task3v2()
    #n, m = map(int, input().split())
    #x = [[True for j in range(m+1)] for i in range(n+1)]
    #x[1][2] = False
    #x[3][4] = False
    #task4(n,m, x)
    task5()
    
if __name__ == "__main__":
    main()
