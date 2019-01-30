
def gen_bin(m, prefix=""):
    if m == 0:
        print(prefix)
    else:
        gen_bin(m-1, prefix+" 0")
        gen_bin(m-1, prefix+" 1")

print(gen_bin(4))

def gn(n, m, prefix=None):
    """
        n: основание системы счисления
        m: колличество чисел
        prefix: 
    """
    if m == 0:
        print(prefix)
        return 
    prefix = prefix or []
    for digits in range(n):
        prefix.append(digits)
        gn(n, m-1, prefix)
        prefix.pop()


def find(number, prefix):
    flag = False
    for item in prefix:
        if item == number:
            flag = True
            break
    return flag

def gp(n, m=-1, prefix=None):
    m = n if m == -1 else m
    prefix = prefix or []
    if m == 0:
        print(*prefix, end=" ")
        return
    for number in range(1, n+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        gn(n, m-1, prefix)
        prefix.pop()
    