from pythonds.basic.stack import Stack


"""
---------------------------------------------------------------------------------------------------------------------
                                                        Part 1
---------------------------------------------------------------------------------------------------------------------
"""


"""
book example
"""
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))


"""
my
"""

def bb(str):

    alist = list(str)
    s = Stack()
    balanced = True
    i = 0

    while i < len(alist):
        if alist[i] == '(':
            s.push(alist[i])
        elif alist[i] == ')':
            if s.isEmpty():
                balanced = False
                break
            s.pop()
        i+=1
    if not s.isEmpty:
        balanced = False
    return balanced

"""
---------------------------------------------------------------------------------------------------------------------
                                                        Part 2
---------------------------------------------------------------------------------------------------------------------
"""

def parChecker2(str):
    s = Stack() # create Stack 
    alist = list(str) # convert string to chars's list
    balanced = True
    index = 0
    # проходимся по списку alist 
    while index < len(alist) and balanced:
        symbol = alist[index]
        if symbol in '([{': # если текущий символ один из данных скобок
            s.push(symbol) # добовляем его в стек
        else: # иначе если текущий символ закрывающая скобка запускаем данный блок
            if s.isEmpty(): # проверяем пуст ли стек, если пуст то это говорит о том что открывающий скоб у нас небыло в строку
                balanced = False # если строка начинается с открывающихся строк то значит скобы не сбалонсированны
            else: # иначе есил стек не пуст и в нем что-то есть
                top = s.pop() # начинаем проверять что в стеке находиться 
                if not matches(top, symbol): # если символ находящийся в стеке (а это открывающая скоба) не совпадает с закрывающей скобой(текущей) 
                    balanced = False # то скобы не сбалонсированы
        index += 1 
    if balanced and s.isEmpty(): # если же всё проходит удачно и стек пуст и скобы сбалонсированы то 
        return True
    else:
        return False


def matches(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)