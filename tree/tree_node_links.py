class BinaryTree:


    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insertLeft(self, newNodeValue):
        if self.left is not None:
            tmp = self.left
            self.left = BinaryTree(newNodeValue)
            self.left.left = tmp
        else:
            self.left = BinaryTree(newNodeValue)


    def insertRight(self, newNodeValue):
        if self.right is not None:
            tmp = self.right
            self.right = BinaryTree(newNodeValue)
            self.right.right = tmp
        else:
            self.right = BinaryTree(newNodeValue)


    def getRootVal(self):
        return self.value

    
    def setRootVal(self, newValue):
        self.value = newValue


    def getLeftChild(self):
        return self.left

    
    def getRightChild(self):
        return self.right
        

def buildTree():
    tree = BinaryTree('a')
    tree.insertRight('b')
    tree.getLeftChild().insertRight('d')

    tree.insertRight('c')
    tree.getRightChild().insertLeft('e')
    tree.getRightChild().insertRight('f')
    
    return tree


def main():
    tree = BinaryTree(1)
    tree.insertLeft(2)
    print(tree.value, tree.left.value)
    tree.insertLeft(3)
    print(tree.value, tree.left.value, tree.left.left.value)

if __name__ == '__main__':
    main()