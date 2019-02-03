from pythonds.trees.binaryTree import BinaryTree


def binaryTree():
    tree = BinaryTree('book')
    tree.insertLeft('chapter 1')
    tree.getLeftChild().insertLeft('section 1.1')
    tree.getLeftChild().insertRight('section 1.2')

    tree.insertRight('chapter 2')
    tree.getRightChild().insertLeft('section 2.1')
    tree.getRightChild().insertRight('section 2.2')
    return tree

# Обход в прямом порядке
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

# Обход в обратном порядке
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

# симметричный обход
# разобрать
def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


def main():
    print('-----------')
    tree = binaryTree()
    inorder(tree)

main()