#
# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBSTRec(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None
        if root.val<L:
            return self.trimBSTRec(root.right, L, R)
        if root.val>R:
            return self.trimBSTRec(root.left, L, R)

        root.left = self.trimBSTRec(root.left, L, R)
        root.right = self.trimBSTRec(root.right, L, R)

        return root

    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None

        while root.val<L or root.val>R:
            root = root.right if root.val<L else root.left

        cur = root
        while cur:
            while cur.left and cur.left.val<L:
                cur.left = cur.left.right
            cur = cur.left
            
        cur = root
        while cur:
            while cur.right and cur.right.val>R:
                cur.right = cur.right.left
            cur = cur.right
        return root


# @lc code=end

