class Set:
    
    def __init__(self):
        self.set = []

    def add(self, data):
        if data not in self.set:
            self.set.append(data)

    def delete(self, indx):
        for i in range(len(self.set)):
            if i == indx:
                del self.set[i]

    def merge(self, _set):
        if isinstance(_set, Set):
            for item in _set:
                if item not in self.set:
                    self.set.append(item)


    def transfer(self, _set):
        tmp = []
        if isinstance(_set, Set):
            for item in _set:
                if item in self.set:
                    tmp.append(item)
        return tmp

    def difference(self, _set):
        tmp = []
        if isinstance(_set, Set):
            for item in self.set:
                if item not in _set:
                    tmp.append(item)
        return tmp

    def sub_set(self, _set):
        tmp = []
        if isinstance(_set, Set):
            for item in _set:
                if item in self.set:
                    tmp.append(item)
        return tmp

    def __str__(self):
        return str(self.set)

set = Set()
set2 = Set()
for i in range(10):
    set.add(i)

for i in range(5, 8):
    set2.add(i)

print(set)
print(set2)

