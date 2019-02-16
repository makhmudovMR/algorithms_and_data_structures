def task1():
    '''
        Найти второй минимальный элемент
        O(n)
    '''
    alist = [5,2,1,7,9]
    _min1 = alist[0]
    _min2 = alist[0]
    for i in range(len(alist)):
        if alist[i] < _min1:
            _min1 = alist[i]
    
    for j in range(len(alist)):
        if alist[j] < _min2 and alist[j] > _min1:
            _min2 = alist[j]
    print(_min1, _min2)


def task2():
    '''
        Отображение элементов не имеющих пары
        (Первые не повторяющиеся целые числа)
        O(n^2)
    '''
    alist = [6,4,3,7,2,7,1,4,7,9,0,4,3,0]
    for i in range(len(alist)):
        for j in range(len(alist)):
            if i != j and alist[i] == alist[j]:
                alist[i] = None
                alist[j] = None
    print(alist)    


def task3():
    '''
        Объединить два отсортированных массива
        O(n)
    '''
    alist1 = [1,2,3,4]
    alist2 = [5,6,7,8,9]
    alist = [None] * (len(alist1) + len(alist2))
    i = 0
    for item in alist1:
        alist[i] = item
        i+=1
    
    for item in alist2:
        alist[i] = item
        i+=1
    print(alist)


def task4():
    '''
        Переставить положительные и отрицательные значения.
    '''
    pass


task3()