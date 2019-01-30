def hash(string, tablesize):
    sum = 0
    for pos in range(len(string)):
        sum = sum + ((pos+1) * ord(string[pos]))
    print(sum)
    return sum % tablesize


print(hash('cat', 11))