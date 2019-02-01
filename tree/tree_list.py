def binaryTree(root):
    return [root, [], []]

def insertLeft(tree, newNode):
    tmp = tree[1]
    if len(tmp) > 1:
        tree[1] = binaryTree(newNode)
        tree[1][1] = tmp
    else:
        tree[1] = binaryTree(newNode)

def insertRight(tree, newNode):
    tmp = tree[2]
    if len(tmp) > 1:
        tree[2] = binaryTree(newNode)
        tree[2][2] = tmp
    else:
        tree[2] = binaryTree(newNode)

#
 
def insertLeft2(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight2(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

# sevice

def getRootVal(tree):
    return tree[0]

def getLeftChild(tree):
    return tree[1]

def getRightChild(tree):
    return tree[2]

def setRootVal(tree, value):
    tree[0] = value


def buildTree():
    tree = binaryTree('a')
    insertLeft(tree, 'b')
    insertRight(getLeftChild(tree), 'd')

    insertRight(tree, 'c')
    insertLeft(getRightChild(tree), 'e')
    insertRight(getRightChild(tree), 'f')
    return tree

def main():
    print(buildTree())

if __name__ == '__main__':
    main()