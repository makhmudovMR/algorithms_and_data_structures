def buble_sort(A):
    """
        Квадратичный алгоритм
        Сортировка метода пузырька 
    """
    i = 0
    while i < len(A):
        j=0
        while j < len(A)-i-1:
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            j+=1
        i+=1
    return A


def test_sort(sort_function):
    A_sort = [i for i in range(6)]
    A = [5,3,4,2,1,0]
    result = sort_function(A)
    print(result)

    print("ok" if result == A_sort else "fail")

test_sort(buble_sort)
