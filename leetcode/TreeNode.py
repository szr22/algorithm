class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root
        self.inOrderTreeArr = []

    def generateInOrder(self, node):
        if not node:
            return
        self.generateInOrder(node.left)
        self.inOrderTreeArr.append(node.val)
        self.generateInOrder(node.right)