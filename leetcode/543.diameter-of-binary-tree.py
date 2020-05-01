#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0

        (left_height, left_longest) = self.get_max_hight(root.left)
        (right_height, right_longest) = self.get_max_hight(root.right)
        return max(left_height + right_height+1, left_longest, right_longest) -1

    def get_max_hight(self, root: TreeNode) -> (int, int):
        if root == None:
            return (0, 0)
        if root.left == None and root.right == None:
            return (1, 1)

        (left_height, left_longest) = self.get_max_hight(root.left)
        (right_height,right_longest) = self.get_max_hight(root.right)
        longest_path = max(left_height + right_height+1, left_longest, right_longest)
        return (max(left_height+1, right_height+1), longest_path)

# @lc code=end

