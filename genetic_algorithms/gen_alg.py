import random
import time
'''
    Генетический алгоритм 
    Поиск экстремума z = f(x, y)
    мы должны найти максимум
'''

def f(x, y):
    return x / ((x**2) +(2*y**2) + 1)


# начальная популяция 
# набор хромосом (x, y) (каждое значение это ген)
alist = [[-2, 0], [-1, -2], [0, 4], [1, 2]]
crossovering = []
i = 0


while i < 100:
    tmp = []
    print('----------------')
    print('хромосомы родителий:', alist)
    for item in alist:
        tmp.append(f(item[0], item[1]))
    print('результаты родителей:', tmp)

    # отбор лидеров
    print('(Максимальный результат) Отбор лидеров по результатам:', end=' ')
    indivIndx1 = tmp.index(max(tmp))
    print(tmp.pop(tmp.index(max(tmp))), end=' ')
    indivIndx2 = tmp.index(max(tmp))
    print(tmp.pop(tmp.index(max(tmp))), end=' ')
    indivIndx3 = tmp.index(max(tmp))
    print(tmp.pop(tmp.index(max(tmp))), end=' ')
    print()

    # скрещивание
    child1 = [alist[indivIndx2][0], alist[indivIndx1][1]]
    child2 = [alist[indivIndx3][0], alist[indivIndx1][1]]
    child3 = [alist[indivIndx1][0], alist[indivIndx2][1]]
    child4 = [alist[indivIndx1][0], alist[indivIndx3][1]]
    alist = [child1, child2, child3, child4]

    print('хромосомы потомства:',alist)

    # мутация
    for _ in range(0, 1):
        alist[random.randint(0, 3)][random.randint(0, 1)] = random.randint(alist[random.randint(0, 3)][random.randint(0, 1)]-10, alist[random.randint(0, 3)][random.randint(0, 1)]+10)
    
    print('потомство подвергнутое мутации:', alist)

    print('----------------------------') 
    i+=1
    time.sleep(2)
    

