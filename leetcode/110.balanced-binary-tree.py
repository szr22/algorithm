#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.checkDepth(root)==-1:
            return False
        return True

    def checkDepth(self, node):
        if not node:
            return 0
        left = self.checkDepth(node.left)
        if left == -1:
            return -1
        right = self.checkDepth(node.right)
        if right == -1:
            return -1

        diff = abs(left-right)
        if diff>1:
            return -1
        else:
            return 1+max(left, right)

# @lc code=end

