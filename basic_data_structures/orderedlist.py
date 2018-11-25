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



class OrderedList:


    def __init__(self):
        self.head = None


    def size(self):
        count = 0
        current = self.head

        while current != None:
            current = current.getNext()
            count+=1
        
        return count


    def isEmpty(self):
        self.head == None


    def remove(self, item):
        prev = None
        curr = self.head
        found = False

        while not found or curr.getNext != None:
            if curr.getData() == item:
                found = True
            else:
                prev = curr
                curr = curr.getNext()
        
        if prev == None:
            self.head = curr.getNext()
        else:
            prev.setNext(curr.getNext())


    def search(self, item):
        curr = self.head
        found = False
        stop = False

        while curr != None and not found and not stop:
            if curr.getData() == item:
                found = True
            else:
                if curr.getData() > item:
                    stop = True
                else:
                    curr = curr.getNext()

        return found


    def add(self, item):
        curr = self.head
        prev = None
    
        stop = False

        while curr.getData() != None or not stop:
            if curr.getData() > item:
                stop = True
            curr = curr.getNext()
        
        temp = Node(item)
        if prev == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(curr)
            prev.setNext(temp)

    def print(self):
        alist = []

        current = self.head
        while current != None:
            alist.append(current.getData())
            current = current.getNext()
        print(alist)
            
mylist = OrderedList()


mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

# mylist.insert(1, 'Hello world')
mylist.print()