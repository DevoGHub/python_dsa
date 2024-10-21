class Tree:
    def __init__(self):
        self.root: TreeNode = None

    def insert(self, value: int):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.root.insert(value)
    
    def getMin(self):
        if self.root is None:
            return None
        return self.root.getMin()
    
    def getMax(self):
        if self.root is None:
            return None
        return self.root.getMax()
    
    def traversePre(self):
        if self.root is not None:
            self.root.traversePre()

    def traverseIn(self):
        if self.root is not None:
            self.root.traverseIn()

    def traversePost(self):
        if self.root is not None:
            self.root.traversePost()


class TreeNode:
    def __init__(self, data: int):
        self.data: int = data
        self.leftChild: TreeNode = None
        self.rightChild: TreeNode = None

    def insert(self, value: int):
        if value < self.data:
            if self.leftChild is None:
                self.leftChild = TreeNode(value)
            else:
                self.leftChild.insert(value)
        else:
            if self.rightChild is None:
                self.rightChild = TreeNode(value)
            else:
                self.rightChild.insert(value)
    
    def getMin(self):
        if self.leftChild is None:
            return self.data
        return self.leftChild.getMin()
    
    def getMax(self):
        if self.rightChild is None:
            return self.data
        return self.rightChild.getMax()
    
    def traversePre(self):
        print(self.data, end=" ")
        if self.leftChild is not None:
            self.leftChild.traversePre()
        if self.rightChild is not None:
            self.rightChild.traversePre()

    def traverseIn(self):
        if self.leftChild is not None:
            self.leftChild.traverseIn()
        print(self.data, end=" ")
        if self.rightChild is not None:
            self.rightChild.traverseIn()

    def traversePost(self):
        if self.leftChild is not None:
            self.leftChild.traversePost()
        if self.rightChild is not None:
            self.rightChild.traversePost()
        print(self.data, end=" ")
    
tree = Tree()
tree.insert(25)
tree.insert(20)
tree.insert(15)
tree.insert(27)
tree.insert(30)
tree.insert(29)
tree.insert(26)
tree.insert(22)
tree.insert(32)

print("min ",tree.getMin())
print("max ",tree.getMax())
tree.traversePre()
print()
tree.traverseIn()
print()
tree.traversePost()
print()