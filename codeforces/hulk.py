n = int(input())

str = ""
count = 1
i = n

while i > 0:
    if count % 2 == 0:
        if i > 1:
            str += "I love that"
        else:
            str += "I love it"
    else:
        if i > 1:
            str += "I hate that"
        else:
            str += "I hate it"
    if not i < 2:
        str += " "
    i-=1
    count+=1

    

print(str)