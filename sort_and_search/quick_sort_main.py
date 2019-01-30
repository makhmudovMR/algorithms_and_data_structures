def qs(alist):
    if len(alist) <= 1:
        return alist
    
    pivot = alist[0]
    left = []
    right = []
    mid = []

    for x in alist:
        if pivot > x:
            left.append(x)
        elif pivot < x:
            right.append(x)
        else:
            mid.append(x)
    
    left_sort = qs(left)
    right_sort = qs(right)

    i = 0
    for x in left_sort+mid+right_sort:
        alist[i] = x
        i+=1
    return alist

print(qs([5,3,7,4,2,2,1]))