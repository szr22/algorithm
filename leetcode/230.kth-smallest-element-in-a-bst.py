#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.cnt = 0
        self.resNode = None
        self.inOrder(root, k)
        return self.resNode.val

    def inOrder(self, node, k):
        if self.cnt == k or not node:
            return
        self.inOrder(node.left, k)
        if self.cnt == k:
            return
        self.cnt += 1
        self.resNode = node
        self.inOrder(node.right, k)

# @lc code=end

