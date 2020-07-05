#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbersStraight(self, root: TreeNode) -> int:
        if not root:
            return 0
        nums = []
        s = ""
        self.dfs(root, s, nums)
        return sum(nums)

    def dfs(self, node, s, nums):
        if not node:
            return
        if self.isLeaf(node):
            s += str(node.val)
            nums.append(int(s))
            return
        s += str(node.val)
        self.dfs(node.left, s, nums)
        self.dfs(node.right, s, nums)

    def isLeaf(self, node):
        if not node:
            return False
        if not node.left and not node.right:
            return True
        return False

    def sumNumbers(self, root: TreeNode) -> int:
        result = [0]
        cr = [0]
        def traverse(node):
            if node.left is None and node.right is None:
                result[0] += cr[0]*10 + node.val
                return
            cr[0] = cr[0]*10 + node.val
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
            cr[0] = cr[0]//10
        if root is not None:
            traverse(root)
        return result[0]
# @lc code=end

