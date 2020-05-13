#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
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
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        res = []
        self.node_str_map = defaultdict(int)
        self.serilize(root, res)
        return res

    def serilize(self, node, res):
        if not node:
            return '#'

        curStr = (
            str(node.val) + ','
            + self.serilize(node.left, res) + ','
            + self.serilize(node.right, res) + ','
        )

        if self.node_str_map[curStr] == 1:
            res.append(node)

        self.node_str_map[curStr] += 1

        return curStr

# @lc code=end

