class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        # self.root = root
        self.inOrderTreeArr = []
        self.preOrderTreeArr = []
        self.postOrderTreeArr = []

    def generateInOrder(self, node):
        if not node:
            return
        self.generateInOrder(node.left)
        self.inOrderTreeArr.append(node.val)
        self.generateInOrder(node.right)

    def generatePreOrder(self, node):
        if not node:
            return
        self.preOrderTreeArr.append(node.val)
        self.generatePreOrder(node.left)
        self.generatePreOrder(node.right)

    def generatePostOrder(self, node):
        if not node:
            self.postOrderTreeArr.append('#')
            return
        self.generatePostOrder(node.left)
        self.generatePostOrder(node.right)
        self.postOrderTreeArr.append(node.val)