#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        n = len(preorder)
        root = TreeNode(preorder[0])
        if n == 1:
            return root
        left = []
        right = []
        for idx in range(1,n):
            if preorder[idx]<root.val:
                left.append(preorder[idx])
            else:
                right.append(preorder[idx])

        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)
        return root

# @lc code=end

