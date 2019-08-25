"""
A python implementation of Binary Search Tree
https://gist.github.com/jakemmarsh/8273963
"""


class Node():
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    def getChildren(self):
        children = []
        if self.leftChild:
            children.append(self.leftChild)
        if self.rightChild:
            children.append(self.rightChild)
        return children


class BST():
    def __init__(self):
        self.root = None
        self.order = []

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root is None:
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if val <= currentNode.val:
            if currentNode.leftChild:
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        else:
            if currentNode.rightChild:
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)

    def find(self, val):
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        if currentNode is None:
            return False
        elif val == currentNode.val:
            return True
        elif val < currentNode.val:
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)

    def transverse(self):
        self.in_order(self.root)

    def in_order(self, currentNode):
        if currentNode is None:
            return
        if currentNode.leftChild:
            if self.in_order(currentNode.leftChild):
                self.order.append(self.in_order(currentNode.leftChild))

        self.order.append(currentNode.val)

        if currentNode.rightChild:
            if self.in_order(currentNode.rightChild):
                self.order.append(self.in_order(currentNode.rightChild))
        return


def main():
    bst = BST()
    for i in range(10, 0, -1):
        bst.insert(i)
    if bst.find(8):
        print('Node 8 exists')
    if not bst.find(20):
        print('Node 20 does not exist')

    # in-order transverse
    bst.transverse()
    print(bst.order)


if __name__ == '__main__':
    main()
