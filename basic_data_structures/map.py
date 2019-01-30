class HashTable:

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots)) #получаем хеш индекс
        if self.slots[hashvalue] == None: #если слот под этим индексом пуст
            self.slots[hashvalue] = key #записыаем данные
            self.data[hashvalue] = data
        else: иначе
            if self.slots[hashvalue] == key: #если же слот не пуст и ключ совпадает с тем ключом под который мы хотим записать данные 
                self.data[hashvalue] = data #перезаписыаем данные
            else: #иначе если ключ не совпадает с нашим ключом
                nextslot = self.rehash(hashvalue, len(self.slots)) #ищем пустой слот или слот который мы хотим перезаписать
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                if self.slots[nextslot] == None: # если мы нашли пустой слот
                    self.slots[nextslot] = key #записыаем данные
                    self.data[nextslot] = data
                else: 
                    self.data[nextslot] = data # иначе перезаписыаем данные


    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots)) стартовый хеш индекс
        
        data = None
        stop = False
        found = False
        position = startslot
        # ищем слот с ключом пока не нашли пустой слот или пока не остановились
        while self.slots[position] != None and not found and not stop: 
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def hashfunction(self, key, size):
        return key%size
    
    def rehash(self, oldhash, size):
        return (oldhash+1) % size


h = HashTable()

h[54] = 'cat'
h[85] = 'hashtable'

print(h.slots)

print(h.data)