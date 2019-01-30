def quick_sort(alist): # [2,3,4,1]
    if len(alist) <= 1:
        return

    barr = alist[0]
    left = []
    mid = []
    right = []

    for i in range(len(alist)):
        if alist[i] < barr:
            left.append(alist[i])
        elif alist[i] > barr:
            right.append(alist[i])
        else: #alist[i] == bar
            mid.append(alist[i]) 
            
    quick_sort(left)
    quick_sort(right) 

    k=0
    for x in left+mid+right:
        alist[k] = x
        k+=1
    return alist

alist = [2,3,4,1]
print(quick_sort(alist))