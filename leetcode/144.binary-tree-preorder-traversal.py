#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

from typing import List

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res

    def preorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.res = []
        self.preorder_trav_recur(root)
        return self.res

    def preorder_trav_recur(self, node: TreeNode):
        if not node:
            return

        self.res.append(node.val)
        self.preorder_trav_recur(node.left)
        self.preorder_trav_recur(node.right)


# @lc code=end

