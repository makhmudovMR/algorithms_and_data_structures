def task1():
    '''Определить, является ли массив подмножеством другого массива.'''
    alist1 = [None, 90, None, 3, None, None]
    alist2 = [5, None, 0, None, None, None]

    flag = False

    for i in range(len(alist1)):
        for j in range(len(alist2)):
            if alist1[i] == alist2[j] and ( alist1[i] != None and alist2[j]!= None):
                flag = True

    print(flag)



def task2():
    '''Проверить, являются ли массивы непересекающимися'''
    alist1 = [None, 90, None, 3, None, None]
    alist2 = [5, None, 0, None, None, None]

    flag = True

    for i in range(len(alist1)):
        for j in range(len(alist2)):
            if alist1[i] == alist2[j] and ( alist1[i] != None and alist2[j]!= None):
                flag = False

    print(flag)


task1()

