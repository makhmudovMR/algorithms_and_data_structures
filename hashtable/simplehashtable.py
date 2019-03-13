def hashFunc(x):
    return x % 10

def insert(table, key, value):
    table[hashFunc(key)] = value

def get(table, key):
    return table[hashFunc(key)]

def main():
    table = [None] * 10

    print(table)
    
    insert(table, 43, 'dog')
    insert(table, 21, 'cat')
    
    print(table)
    
    print('<-----we are get---->')
    
    print('key 43: ', get(table, 43))
    print('key 21: ', get(table, 21))
    print('key 37: ', get(table, 37))

main()