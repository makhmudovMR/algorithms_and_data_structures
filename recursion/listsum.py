def f(alist):
    sum = 0
    for item in alist:
        sum += item
    return sum


def f2(alist):
    if len(alist) <= 1:
        return alist[0]
    else:
        return alist[0] + f2(alist[1:])
        '''
        iter 1 from rear
        6 + 7
        
        '''
    

alist = [1,2,3,4,5,6,7]

print(f(alist))
print(f2(alist, 0))