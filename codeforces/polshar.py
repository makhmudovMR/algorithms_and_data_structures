def is_simple_n(n):
    flag = True

    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    return flag


def main():
    n = int(input())
    m = 1
    flag = True
    while flag:
        if not is_simple_n((n * m) + 1):
            flag = False
            break
        else:
            m+=1
    print(m)

main()