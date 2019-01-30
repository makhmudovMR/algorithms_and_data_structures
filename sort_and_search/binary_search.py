def binary_search(alist, item):
    found = False
    while len(alist) > 1 and not found:
        mid = len(alist) // 2
        print(alist)
        if alist[mid] > item:
            alist = alist[:mid]
        elif alist[mid] < item:
            alist = alist[mid:]
        else:
            found = True
    return found


def bin_search_recursion(alist, item):
    print(alist)
    if len(alist) <= 1:
        return alist[0] == item
    mid = len(alist)//2
    if alist[mid] > item:
        return bin_search_recursion(alist[:mid], item)
    elif alist[mid] < item:
        return bin_search_recursion(alist[mid:], item)
    else:
        return True

alist = [i for i in range(11)]
print(bin_search_recursion(alist, 3))
print(binary_search(alist,3))
