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


class UnorderedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.len +=1

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        assert self.len > 0, "Список не содержит элементов"
        current = self.head
        previous = None
        found = False
        while current != None and  not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.len -=1


    def append(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(item)
        self.len += 1
        
    def reverse(self):
        # https://www.youtube.com/watch?v=D7y_hoT_YZI
        # https://www.geeksforgeeks.org/reverse-a-linked-list/
        """
            Инверсия связного списка
            method:
                prev->curr->next => prev<-curr<-next
        """
        prev = None
        curr = self.head
        next = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def __str__(self):
        str = ""
        curr = self.head
        while curr != None:
            str += "{}->".format(curr.data)
            curr = curr.next
        str=str[:-2]
        return str


mylist = UnorderedList()
# mylist.remove(5)
for i in range(10):
    mylist.append(i)
print(mylist)
# mylist.remove(5)
print(mylist)
mylist.reverse()
print(mylist)