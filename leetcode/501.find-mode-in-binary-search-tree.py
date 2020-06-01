#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#
from collections import defaultdict
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findModeExtraSpace(self, root: TreeNode) -> List[int]:
        res = []
        self.mx = 0
        counterMap = defaultdict(int)
        self.inorderExtraSpace(root, counterMap)
        for k, v in counterMap.items():
            if v == self.mx:
                res.append(k)
        return res

    def inorderExtraSpace(self, node, counterMap):
        if not node:
            return
        self.inorderExtraSpace(node.left, counterMap)
        counterMap[node.val] += 1
        self.mx = max(self.mx, counterMap[node.val])
        self.inorderExtraSpace(node.right, counterMap)

    def findMode(self, root: TreeNode) -> List[int]:
        self.res = []
        self.mx = 0
        self.cnt = 1
        self.pre = None
        self.inorder(root)
        return self.res

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        if self.pre:
            if node.val == self.pre.val:
                self.cnt += 1
            else:
                self.cnt = 1
        if self.cnt >= self.mx:
            if self.cnt > self.mx:
                self.res = []
            self.res.append(node.val)
            self.mx = self.cnt

        self.pre = node

        self.inorder(node.right)

# @lc code=end

