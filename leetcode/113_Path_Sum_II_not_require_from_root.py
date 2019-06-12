# Given a binary tree and a sum, find all paths where each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

from typing import List
from TreeNode import TreeNode

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        cur = []
        self.helper(root, res, cur, target)
        return res

    def helper(self, node, res, cur, target):
        if not node:
            return
        cur.append(node.val)
        sumNum = 0
        for i in range(len(cur)-1, -1, -1):
            sumNum += cur[i]
            if sumNum == target:
                tmpRes = []
                for j in range(i,len(cur)):
                    tmpRes.append(cur[j])
                res.append(tmpRes)
        self.helper(node.left, res, cur, target)
        self.helper(node.right, res, cur, target)
        cur.pop()



root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

target = 22

res = Solution().pathSum(root, target)
print(res)