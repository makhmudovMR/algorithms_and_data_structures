t = [1,2, [3,4, [5]]]

def extract(li, result=[]):
    for i in li:
        if isinstance(i, list):
            extract(i, result)
        else:
            result.append(i)
    return result

print(extract(t))