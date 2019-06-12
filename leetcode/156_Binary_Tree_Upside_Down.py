from TreeNode import TreeNode

class Solution:
    def binaryTreeUpsideDown(self, node: TreeNode) -> TreeNode:
        if not node or not node.left:
            return node
        root = self.binaryTreeUpsideDown(node.left)
        l, r = node.left, node.right
        l.right = node
        l.left = r
        node.right = None
        node.left = None

        return root

    def binaryTreeUpsideDownRecur(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        l = root.left
        r = root.right
        root.left = None
        root.right = None
        while l:
            newL = l.left
            newR = l.right
            l.left = r
            l.right = root
            root = l
            l = newL
            r = newR
        return root

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

from TreeNode import Tree
tree = Tree(root)
tree.generateInOrder(root)
print(tree.inOrderTreeArr)

rootNew = Solution().binaryTreeUpsideDown(root)
newTree = Tree(rootNew)
newTree.generateInOrder(rootNew)
print(newTree.inOrderTreeArr)

# rootNewRecur = Solution().binaryTreeUpsideDownRecur(root)
# newTreeRecur = Tree(rootNewRecur)
# newTreeRecur.generateInOrder(rootNewRecur)
# print(newTreeRecur.inOrderTreeArr)
