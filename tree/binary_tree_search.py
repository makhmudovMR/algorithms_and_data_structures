'''
    BinaryTreeSearch
'''

class TreeNode:

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.payload  = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    # есть ли левый потомок
    def hasLeftChild(self):
        return self.leftChild

    # есть ли правый потомок
    def hasRightChild(self):
        return self.rightChild

    # является ли текущий узел левым потомком своего родителя
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    # является ли узел правым потомком своего родителя
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    # явялется ли узел корнем дерева
    def isRoot(self):
        return not self.parent
    
    # является ли узел листом дерева
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    # имеет ли узел хоть одного потомка
    def hasAnyChildren(self):
        return  self.rightChild or self.leftChild

    # имеет ли узел оба потомка
    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    # заменяем данные узла 
    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinaryTreeSearch:
    
    def __init__(self):
        self.root = None
        self.size = 0


    def length(self):
        return self.size


    def __len__(self):
        return self.size


    def __iter__(self):
        return self.root.__iter__()


    def __setitem__(self, k, v):
        self.put(k, v)

    
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size +=1


    def _put(self, key, val, currNode):
        if key < currNode.key:
            if currNode.hasLeftChild():
                self._put(key, val, currNode.leftChild)
            else:
                currNode.leftChild = TreeNode(key, val, parent=currNode)
        else:
            if currNode.hasRightChild():
                self._put(key, val, currNode.rightChild)
            else:
                currNode.rightChild = TreeNode(key, val, parent=currNode)
