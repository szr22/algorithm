#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        sum = 0
        if root.val>=L and root.val<=R:
            sum += root.val
        if root.val>=L:
            sum += self.rangeSumBST(root.left, L, R)
        if root.val<=R:
            sum += self.rangeSumBST(root.right, L, R)
        return sum
# @lc code=end

