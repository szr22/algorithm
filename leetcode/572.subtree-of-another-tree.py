#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not t or not s:
            return False

        res = False
        if s.val == t.val:
            res = self.is_same_tree(s, t)
            if res == True:
                return res

        return (
            self.isSubtree(s.left, t)
            or self.isSubtree(s.right, t)
        )

    def is_same_tree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False

        if s.val == t.val:
            return (
                self.is_same_tree(s.left, t.left)
                and self.is_same_tree(s.right, t.right)
            )

        return False
# @lc code=end

