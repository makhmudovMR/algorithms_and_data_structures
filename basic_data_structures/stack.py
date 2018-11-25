class Stack:

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    s = Stack()
    s.push(4)
    s.push('dog')
    print(s.isEmpty())
    print(s.size())
    print(s.peek())
    print(s.pop())
    print(s.size())
    print(s.pop())
    print(s.size())
    print(s.isEmpty())