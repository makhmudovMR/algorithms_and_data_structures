n = int(input())
alist = []

for i in range(n):
    alist.append(input())

for i in range(len(alist)):
    if len(alist[i]) > 10:
        alist[i] = alist[i][0] + str(len(alist[i])-2) + alist[i][len(alist[i])-1]

for item in alist:
    print(item)