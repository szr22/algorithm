#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        self.res = ''
        if not t:
            return self.res
        self.perOrder(t)
        return self.res

    def perOrder(self, t):
        self.res += str(t.val)
        if t.left:
            self.res += '('
            self.perOrder(t.left)
            self.res += ')'
        else:
            if t.right:
                self.res += '()'

        if t.right:
            self.res += '('
            self.perOrder(t.right)
            self.res += ')'

# @lc code=end

