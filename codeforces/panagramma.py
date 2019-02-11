n = int(input())
string = input()

memory = [False for _ in range(ord('a')-97, ord('z')-97)]

for c in string:
    c=c.lower()
    if not memory[ord(c)-97]:
        memory[ord(c)-97] = True
    
flag = True

for item in memory:
    if not item:
        flag = False

if flag:
    print('YES')
else:
    print('NO')
