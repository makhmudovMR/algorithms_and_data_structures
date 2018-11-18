def anagramSolution1(s1, s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    # запускаем цикл по s1 (stillOK переменная для выхода из цикла в случаем если не найдуться совпадения)
    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        # запускаем цикл по alist (found переменная которая говорит найдено ли совпадение или нет)
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1
    print(alist)
    return stillOK


def anagramSolutions2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(alist1) and matches:
        if alist1[pos] == alist2[pos]:
            pos +=1
        else:
            matches = False
        
        return matches


def anagramSolution4(s1, s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    
    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j+=1
        else:
            stillOK=False
    return stillOK


anagramSolution1('hello', 'lleho')