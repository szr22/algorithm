#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
from TreeNode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.MIN_NUM = -2147483648
        self.maxSum = self.MIN_NUM

    def maxPathSum(self, root: TreeNode) -> int:
        self.pathSum(root)
        return self.maxSum

    def pathSum(self, root: TreeNode) -> int:
        if not root:
            return self.MIN_NUM
        if not root.right and not root.left:
            self.maxSum = max(self.maxSum, root.val)
            return root.val
        left = self.pathSum(root.left)
        right = self.pathSum(root.right)
        print(left, right, left+right+root.val, self.maxSum)
        self.maxSum = max(
            left+root.val,
            right+root.val,
            left+right+root.val,
            root.val,
            self.maxSum
        )

        return max(left, right, 0)+root.val

# @lc code=end

