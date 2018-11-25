from pythonds.basic.stack import Stack

def convert(n):
    stack = Stack()
    alist = []

    while n >= 1:
        x = n // 2
        tmp = n - (x * 2)
        print(tmp) 
        stack.push(tmp)
        n = x
    
    while not stack.isEmpty():
        alist.append(stack.pop())
    return alist

print(convert(42))
        
