n = input()
alist = list(map(int, input().split()))

max_in = max(alist)
count = 0
for item in alist:
    count+= max_in - item

print(count)