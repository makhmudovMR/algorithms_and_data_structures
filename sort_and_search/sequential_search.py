def search(alist, el):
    i = 0
    found = False

    while i < len(alist) and not found:
        if alist[i] == el:
            found = True
        else:
            i+=1
    return found


def test_search():
    alist = [i for i in range(20)]
    el = 8

    print('ok' if search(alist, el) else 'fail')

test_search()


def oss(alist, item):
    """
        Ordered Sequential Search
    """
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1
    
    return found

