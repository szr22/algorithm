#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total = 0
        self.helper(root)
        return root

    def helper(self, node):
        if not node:
            return
        self.helper(node.right)
        node.val += self.total
        self.total = node.val
        self.helper(node.left)

# @lc code=end

