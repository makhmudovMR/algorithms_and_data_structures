def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left=left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    result = result + right + left
    return result

def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left = merge_sort(alist[:mid])
    print("left: ", left)
    right = merge_sort(alist[mid:])
    print("right: ", right)
    return merge(left, right)

alist = [6,4,5,3,1,2]
print(merge_sort(alist))