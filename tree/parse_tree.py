from pythonds.trees.binaryTree import BinaryTree
from pythonds.basic.stack import Stack
import re


def buildTree(string):
    string = string.split()
    tree = BinaryTree('')
    stack = Stack()
    curr = tree
    stack.push(tree)
    for c in string:
        if c == '(':
            stack.push(curr)
            curr.insertLeft('')
            curr = curr.getLeftChild()
        elif c in '+-*/':
            stack.push(curr)
            curr.setRootVal(c)
            curr.insertRight('')
            curr = curr.getRightChild()
        elif re.match(r'\d', c):
            curr.setRootVal(c)
            curr = stack.pop()
        elif c == ')':
            curr = stack.pop()
    return tree

class operator:

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

operator = operator()


def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return int(parseTree.getRootVal())


def calculateTree(tree):
    if re.match(r'\d', tree.getLeftChild().getRootVal()) and re.match(r'\d', tree.getRightChild().getRootVal()):
        l = int(tree.getLeftChild().getRootVal())
        r = int(tree.getRightChild().getRootVal())
        if tree.getRootVal() == '+':
            tree.setRootVal(str(l + r))
            tree.insertLeft(None)
            tree.insertRight(None)
        elif tree.getRootVal() == '-':
            tree.setRootVal(str(l - r))
            tree.insertLeft(None)
            tree.insertRight(None)
        elif tree.getRootVal() == '*':
            tree.setRootVal(str(l * r))
            tree.insertLeft(None)
            tree.insertRight(None)
        elif tree.getRootVal() == '/':
            tree.setRootVal(str(l / r))
            tree.insertLeft(None)
            tree.insertRight(None)
    else:
        if not re.match(r'\d', tree.getLeftChild().getRootVal()):
            calculateTree(tree.getLeftChild())
        elif not re.match(r'\d', tree.getRightChild().getRootVal()):
            calculateTree(tree.getRightChild())

def main():
    tree = buildTree('( ( 10 + 2 ) + 3 )')
    tree.postorder()
    print('---')
    print(evaluate(tree))

if __name__ == '__main__':
    main()
