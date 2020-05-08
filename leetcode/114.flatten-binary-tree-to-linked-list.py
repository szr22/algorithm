#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def flattenRec(self, root: TreeNode) -> None:
        if not root:
            return

        self.flattenRec(root.left)
        self.flattenRec(root.right)

        if root.left:
            cur = root.left
            while cur.right:
                cur = cur.right
            cur.right = root.right
            root.right = root.left
            root.left = None

    def flatten(self, root):
        cur = root
        while cur:
            if cur.left:
                tmp = cur.left
                while tmp.right:
                    tmp = tmp.right
                tmp.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
# @lc code=end

