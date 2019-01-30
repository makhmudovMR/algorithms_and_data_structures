# вместимость хеш-таблицы
INITIAL_CAPACITY = 50 

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return "<Node: ({}, {}), next: {}>".format(self.key, self.value, self.next!=None)

    def __repr__(self):
        return str(self)

class HashTable:

    def __init__(self):
        """
            Инициализируем хеш-таблицу
        """
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        """
            Генерируем хеш для ключа
            Input: key-string
            Output: Index from 0 to self.capacity 
        """
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum
    
    def insert(self, key, value):
        """
            Вставляет пару ключ значение в хеш-таблицу
        """

        self.size+=1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def find(self, key):
        """
            Ищет значение по заданому ключу
        """
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value


    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]

        prev = None
        while node != None and node.key != key:
            prev = node
            node = node.next
        
        if node is None:
            return None
        else:
            self.size-=1
            result = node.value
            if prev is None:
                self.buckets[index] = node.next # May be None, or the next match
            else:
                prev.next = prev.next.next # LinkedList delete by skipping over
            return result


h = HashTable()
h.insert('magomed', 55)
print(h.buckets)
print(h.find('magomed'))