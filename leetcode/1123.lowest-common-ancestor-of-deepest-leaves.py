#
# @lc app=leetcode id=1123 lang=python3
#
# [1123] Lowest Common Ancestor of Deepest Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxDepth = 0
        self.res = None

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.postOrder(root, 0)
        return self.res

    def postOrder(self, root, depth):
        if not root:
            return depth-1
        leftDepth = self.postOrder(root.left, depth+1)
        rightDepth = self.postOrder(root.right, depth+1)

        if leftDepth==rightDepth and leftDepth>=self.maxDepth:
            self.res = root
            self.maxDepth = leftDepth

        return max(leftDepth, rightDepth)

# @lc code=end

