import re

from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree


def buildTree(string):
    eq = string.split()
    stack = Stack()
    tree = BinaryTree('')
    stack.push(stack)
    curr = tree
    for item in eq:
        if item == '(':
            curr.insertLeft('')
            stack.push(curr)
            curr = curr.getLeftChild()
        elif re.match(r'\d', item):
            curr.setRootVal(item)
            curr = stack.pop()
        elif item in ['+', '-', '/', '*']:
            curr.setRootVal(item)
            curr.insertRight('')
            stack.push(curr)
            curr = curr.getRightChild()
        elif item == ')':
            curr = stack.pop()
        else:
            raise ValueError
    return tree # это всего лишь ссылка на корневую ноду (мы возварщаем корневую ноду)
            
def calculate_tree(tree):
    if re.match(r'\d', tree.getLeftChild().getRootVal()) and re.match(r'\d', tree.getRightChild().getRootVal()):
        l = int(tree.getLeftChild().getRootVal())
        r = int(tree.getRightChild().getRootVal())
        if tree.getRootVal() == '+':
            tree.setRootVal(l + r)
        elif tree.getRootVal() == '-':
            tree.setRootVal(l-r)
        elif tree.getRootVal() == '*':
            tree.setRootVal(l*r)
        elif tree.getRootVal() == '/':
            tree.setRootVal(l/r)
    else:
        if not re.match(r'\d', tree.getLeftChild().getRootVal()):
            calculate_tree(tree.getLeftChild())
        if not re.match(r'\d', tree.getRightChild().getRootVal()):
            calculate_tree(tree.getRightChild())

    l = int(tree.getLeftChild().getRootVal())
    r = int(tree.getRightChild().getRootVal())
    if tree.getRootVal() == '+':
        tree.setRootVal(l + r)
    elif tree.getRootVal() == '-':
        tree.setRootVal(l-r)
    elif tree.getRootVal() == '*':
        tree.setRootVal(l*r)
    elif tree.getRootVal() == '/':
        tree.setRootVal(l/r)

def main():
    tree = buildTree('( ( 10 + 10 ) - ( 10 * 3 ) )')
    

    calculate_tree(tree)
    # tree.postorder()
    print(tree.getRootVal())



if __name__ == '__main__':
    main()
