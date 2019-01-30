class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    """
         Linked List description
    """
    def __init__(self):
        self.head = Node()

    def insert(self, data):
        new_node = Node(data)
        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = new_node

    def lenght(self):
        curr = self.head
        total = 0
        while curr.next:
            total+=1
            curr = curr.next
        return total

    def display(self):
        curr = self.head
        elem = []
        while curr.next:
            curr = curr.next
            elem.append(curr.data)
        return elem

    def get(self, indx):
        in_indx = 0
        curr = self.head
        while curr.next:
            curr = curr.next
            if in_indx == indx:
                return curr.data
            in_indx += 1

    def delete(self, indx):
        indx_in = 0
        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next
            if indx_in == indx:
                if curr.next:
                    prev.next = curr.next
                else:
                    prev.next = None
            indx_in += 1

help(LinkedList)

ll = LinkedList()
for i in range(10):
    ll.insert(i)
# print(ll.get(4))
ll.delete(9)
print(ll.display())