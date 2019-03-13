

class HashMap:


    def __init__(self, size=55):
        self.memory = [None] * size
        self.size = size


    def getHash(self, key):
        summ = 0
        i = 0
        for c in str(key):
            summ += ord(c) + i
            i+=1
        return summ % self.size


    def add(self, key, value):
        index = self.getHash(key)
        if self.memory[index] == None:
            self.memory[index] = [[key, value]]
        else:
            flag = True
            for i in range(len(self.memory[index])):
                if self.memory[index][i][0] == key:
                    self.memory[index][i][1] = value
                    flag = False
            if flag:
                self.memory[index].append([key, value])
                

    def get(self, key):
        index = self.getHash(key)
        if self.memory[index] is None:
            return None
        for item in self.memory[index]:
            if item[0] == key:
                return item[1]


    def delete(self, key):
        index = self.getHash(key)
        if self.memory[index] != None and len(self.memory[index]) == 1:
            self.memory[index] = None
        else:
            for i in range(len(self.memory[index])):
                if self.memory[index][i][0] == key:
                    mark = i
            del self.memory[index][mark]


    def print(self):
        pass


def main():
    hashmap = HashMap()
    hashmap.add('dog', 'wof')
    hashmap.add('cat', 'may')
    hashmap.add('god', 'im creator')
    # print(hashmap.memory)
    # print('------')

    hashmap.add('dog', 'gav gav')
    print(hashmap.memory)

    print('------')

    hashmap.delete('dog')
    print(hashmap.memory)
    hashmap.delete('god')
    print(hashmap.memory)
    print('<-----test---->')

    print(hashmap.get('god'))


main()