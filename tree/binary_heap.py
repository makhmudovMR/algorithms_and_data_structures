class BinHeap:

    def __init__(self):
        self.heap = [0]
        self.currSize = 0

    # перемещает узел i на верх пока он больше своих родителей
    def percUp(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i//2]:
                tmp = self.heap[i//2]
                self.heap[i//2] = self.heap[i]
                self.heap[i] = tmp
            i = i // 2

    # вставляет новый элемент и востанавливает структуру
    def insert(self, k):
        self.heap.append(k)
        self.currSize+=1
        self.percUp(self.currSize)

    # возвращает наименьшего ребёнка из двух детей
    def minChild(self, i):
        if i * 2 + 1 > self.currSize:
            return i * 2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
    # спускает элемент пока он больше своих детей
    def percDown(self, i):
        while (i * 2) <= self.currSize:
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:
                tmp = self.heap[mc]
                self.heap[mc] = self.heap[i]
                self.heap[i] = tmp
            i = mc
    
    def delMin(self):
        retval = self.heap[1]
        self.heap[1] = self.heap[self.currSize]
        self.currSize -= 1
        self.heap.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currSize = len(alist)
        self.heap = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i = i - 1