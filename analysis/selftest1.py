import random

arr2 = list([random.randint(0,9) for i in range(0,10)])

def f1(arr):
    overallmin = arr[0]
    for i in arr:
        is_smallest = True
        for j in arr:
            if i > j:
                is_smallest = False
        if is_smallest:
                overallmin = i
    return overallmin
            


def f2(arr):
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min


print('list: ', arr2)
print('O(n^2):', f1(arr2))
print('O(n):', f2(arr2))