class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            tmp = self.head
            self.head = Node(data)
            self.head.setNext(tmp)

    def printList(self):
        curr = self.head
        while curr != None:
            print(curr.getData(), end=' ')
            curr = curr.getNext()
    
def task1():
    '''
        Разворот связного списка.
    '''
    linkedList = LinkedList()
    for i in range(10):
        linkedList.insert(i)
    print('-----')
    linkedList.printList()

    prev = None
    curr = linkedList.head
    next = None

    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    linkedList.head = prev
    
    print('----')
    linkedList.printList()
        

def task2():
    '''

    '''
    linkedList = LinkedList()
    for i in range(10):
        linkedList.insert(i)
    print('-----')
    linkedList.printList()
    curr = linkedList.head
    while curr.next != None:
        curr = curr.next

    curr.next = linkedList.head

    flag = False
    curr = linkedList.head.next
    tmp = linkedList.head
    while curr != None:
        if tmp is curr:
            flag = True
            break
        curr = curr.next
    print(flag)

def task3():
    linkedList = LinkedList()
    for i in range(10):
        linkedList.insert(i)
    print('---------')
    linkedList.printList()
    print('---------')
    N = 8

    size = 1
    curr = linkedList.head
    while curr.next != None:
        curr = curr.next
        size +=1


    print(size)
    i = 0
    curr = linkedList.head
    while i != (size - N):
        curr = curr.next
        i+=1

    print(curr.getData())


task3()