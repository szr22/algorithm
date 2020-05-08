#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
import TreeNode
from typing import List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.buildTreeRec(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

    def buildTreeRec(self, preorder, pLeft, pRight, inorder, iLeft, iRight):
        if pLeft>pRight or iLeft>iRight:
            return None

        i = 0
        # find root
        for i in range(iLeft, iRight+1):
            if preorder[pLeft] == inorder[i]:
                break
        cur = TreeNode(preorder[pLeft])
        cur.left = self.buildTreeRec(preorder, pLeft+1, pLeft+i-iLeft, inorder, iLeft, i-1)
        cur.right = self.buildTreeRec(preorder, pLeft+i-iLeft+1, pRight, inorder, i+1, iRight)

        return cur

# @lc code=end

