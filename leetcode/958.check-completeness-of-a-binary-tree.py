#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#
from collections import deque
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = deque([root])
        missing = False
        while queue:
            n = len(queue)
            # only take cur len of node, append rest in the end
            while n > 0:
                n -= 1
                node = queue.popleft()
                if node:
                    if missing:
                        return False
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    missing = True
        return True


# @lc code=end

