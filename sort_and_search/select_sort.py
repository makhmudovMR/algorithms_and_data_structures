def select_sort(alist):
    """
        Сортировка методом выбора 
        Квадратичная сортировка
    """
    i = 0
    
    while i < len(alist):
        j = i
        while j < len(alist):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
            j+=1
        i+=1
    return alist

def select_sort2(alist):
    i = 0
    while i < len(alist):
        j = i
        min = j
        while j < len(alist):
            if alist[i] > alist[j]:
                min = j
            j+=1
        alist[i], alist[min], = alist[min], alist[i]
        i+=1
    return alist
    

alist = [4,5,2,1,3]
print(select_sort(alist))
print(select_sort2(alist))