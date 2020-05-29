#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        if (
            (p.left and not q.left)
            or (not p.left and q.left)
            or (p.right and not q.right)
            or (not p.right and q.right)
        ):
            return False


        if p.val != q.val:
            return False
        if p.left and q.left:
            if not self.isSameTree(p.left, q.left):
                return False

        if p.right and q.right:
            if not self.isSameTree(p.right, q.right):
                return False
        return True
# @lc code=end

