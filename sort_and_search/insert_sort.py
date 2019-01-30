def insert_sort(alist):
    """
        Сортировка вставками
        Квадратичная сортировка 
    """
    i = 0
    while i < len(alist):
        j = i
        while j > 0:
            if alist[j-1] > alist[j]:
                alist[j-1], alist[j] = alist[j], alist[j-1]
            j-=1
        i+=1
    return alist

alist = [7,3,4,5,1,2,6]

print(insert_sort(alist))

