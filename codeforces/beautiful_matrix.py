matrix = [list(map(int, input().split())) for i in range(5)]
location = None

flag = True
i = 0

while i < len(matrix) and flag:
    j = 0
    while j < len(matrix[i]) and flag:
        if matrix[i][j] == 1:
            location = [i, j]
            flag = False
        j+=1
    i+=1

res = abs(location[0] - 2) + abs(location[1] - 2)
print(res)