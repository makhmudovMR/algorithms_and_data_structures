def generate_matrix(i, j):
    matrix = [[0] * j for _ in range(i)]
    return matrix

def print_matrix(matrix):
    string = ''
    for row in matrix:
        string += ''.join([str(e) for e in row]) + '\n'
    print(string)

def sub_matrix(matrix, i1, j1, i2, j2):
    # i = y
    # j = x
    tmp = j1
    while i1 <= i2:
        j1 = tmp
        while j1 < j2:
            matrix[i1][j1] = 1
            j1+=1
        i1+=1
    return matrix



matrix = generate_matrix(40, 40)
print_matrix(sub_matrix(matrix, 4,4, 10,10))
