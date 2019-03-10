class Node:

    def __init__(self, value=None):
        self.value = value
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, currNode):
        if value < currNode.value:
            if currNode.leftChild == None:
                currNode.leftChild = Node(value)
            else:
                self._insert(value, currNode.leftChild)
        elif value > currNode.value:
            if currNode.rightChild == None:
                currNode.rightChild = Node(value)
            else:
                self._insert(value, currNode.rightChild)
        else:
            print('Узел уже находится в дереве!')

    '''
    def search(self, value):
        if self.root.value == value:
            return True
        else:
            return self._search(value, self.root)

    def _search(self, value, currNode):
        if value == currNode.value:
            return True
        elif value < currNode.value:
            if currNode.leftChild is not None:
                return self._search(value, currNode.leftChild)
        elif value > currNode.value:
            if currNode.leftChild is not None:
                return self._search(value, currNode.rightChild)
    '''

    def search(self, value):
        if self.root!= None:
            return self._search(value, self.root)
        else:
            return False
    
    def _search(self, value, currNode):
        if value == currNode.value:
            return True
        elif value < currNode.value and currNode.leftChild != None:
            return self._search(value, currNode.leftChild)
        elif value > currNode.value and currNode.rightChild != None:
            return self._search(value, currNode.rightChild)
        return False

        
    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, currNode, currHeight):
        if currNode == None:
            return currHeight
        leftHeight = self._height(currNode.leftChild, currHeight+1)
        rightHeihgt = self._height(currNode.rightChild, currHeight+1)
        return max(leftHeight, rightHeihgt)

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)
    
    def _print_tree(self, currNode):
        if currNode != None:
            self._print_tree(currNode.leftChild)
            print(str(currNode.value)) 
            self._print_tree(currNode.rightChild)

def fill_tree(tree):
    from random import randint
    for _ in range(100):
        curr_elem = randint(0, 1000)
        tree.insert(curr_elem)
    return tree

def main():
    tree = BinarySearchTree()
    tree = fill_tree(tree)
    print(tree.root.value)
    tree.print_tree()
    print('------')
    print(tree.height())
    print('---------')
    for i in range(100):
        
        print(tree.search(i), end=' ')

main()