#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        queue = []
        queue.append([root, 1])
        while queue:
            if len(queue) == 1:
                queue[0][1] = 1
            left = queue[0][1]
            right = left
            n = len(queue)
            for _ in range(n):
                node, right = queue.pop(0)
                if node.left:
                    queue.append([node.left, right*2])
                if node.right:
                    queue.append([node.right, right*2+1])
            res = max(res, right-left+1)

        return res
# @lc code=end

