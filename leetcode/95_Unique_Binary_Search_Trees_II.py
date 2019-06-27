# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

# Example:

# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

from TreeNode import TreeNode, Tree
from typing import List

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generateTree(1, n)
        
    def generateTree(self, l, r):
        res = []
        if l > r:
            # res.append([None])
            # return res
            return [None]
        for i in range(l, r+1):
            l_tree = self.generateTree(l, i-1)
            r_tree = self.generateTree(i+1, r)
            for j in range(len(l_tree)):
                for k in range(len(r_tree)):
                    node = TreeNode(i)
                    node.left = l_tree[j]
                    node.right = r_tree[k]
                    res.append(node)
        return res

class Solution2:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if (n == 0): return []
        dp = [None] * (n+1)
        dp[0] = [None]
        for i in range(1, n+1):
            dp[i] = []
            for j in range(i):
                for left in dp[j]:
                    for right in dp[i-j-1]:
                        root = TreeNode(j+1)
                        root.left = left
                        root.right = self.copy(right, j + 1)
                        dp[i].append(root)
        return dp[n]
    def copy(self, root, delta):
        if (root == None): return root
        node = TreeNode(root.val + delta)
        node.left = self.copy(root.left, delta)
        node.right = self.copy(root.right, delta)
        return node

n = 3
res = Solution2().generateTrees(n)
# print(res)
for node in res:
    t = Tree()
    t.generatePostOrder(node)
    print(t.postOrderTreeArr)
