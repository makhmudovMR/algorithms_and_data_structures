def insert_sort(A):
    """Сортировка списка A методом вставки"""
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k] < A[k-1]:
            A[k], A[k-1] = A[k-1], A[k]
            k-=1
    return A

def select_sort(A):
    """Сортировка списка A методом выбора """
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]
    return A

def buble_sort(A):
    """Сортировка списка A методом пузырька """
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
    return A


def test_sort(sort_algorithm):

    print('testcase {}: '.format(sort_algorithm.__name__), end='')
    A = [4,2,5,1,3]
    A_sorted = [1,2,3,4,5]
    result = sort_algorithm(A)
    print("Ok" if result == A_sorted else "Fail", end="\n")

if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(select_sort)
    test_sort(buble_sort)