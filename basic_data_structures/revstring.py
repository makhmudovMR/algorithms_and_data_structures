from pythonds.basic.stack import Stack

def funcRevString(str):
    alist = list(str)
    s = Stack()
    alist2 = []

    for i in alist:
        s.push(i)
    
    while not s.isEmpty():
        alist2.append(s.pop())
    
    return ''.join(alist2)

print(funcRevString("Hello World"))