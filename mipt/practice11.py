import random 
random.seed()

def fib(n, memory):
    if n <= 1:
        return 1
    if memory[n] != None:
        return memory[n]
    memory[n] = fib(n-1, memory) + fib(n-2, memory)
    return memory[n]



def grig(n):
    """
    +1
    +2
    +3
    """
    F = [0] * (n+1)
    F[1] = 1
    for i in range(2,n+1):
        F[i] = sum(F[max(0, i-2):i])
    print(F)


def grig2(n):
    """
    +1
    +2
    *3
    """
    F = [0] * (n+1)
    F[0] = 0
    F[1] = 1
    F[2] = 1
    for i in range(3,n+1):
        F[i] = F[i-1] + F[i-2]
        if i % 3 == 0:
            F[i] += F[i//3]
    print(F)

def grig3(n, price=[]):
    price[0], price[1]= 0, 0
    P = [0] * (n+1)
    C = [0] * (n+1)
    C[2] = price[2]
    for i in range(3,n+1):
        C[i] = min(C[i-1],C[i-2]) + price[i]
        if C[i-1] > C[i-2]:
            P[i] = i-2
        else:
            P[i] = i-1
    print(C,"min cost")
    print(price,"price")
    print(P, "prev")
    

    
        

def main():
    #grig(10)
    #grig2(10)
    grig3(10, [random.randint(0,6) for _ in range(0, 11)])

if __name__ == "__main__":
    main()
