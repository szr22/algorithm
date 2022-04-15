#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None

        middle = (len(nums)//2)

        root = TreeNode(nums[middle])
        root.left = self.sortedArrayToBST(nums[:middle])
        root.right = self.sortedArrayToBST(nums[middle+1:])

        return root

# @lc code=end

class Solution2:
    def sortedArrayToBST(self, nums):
        root = TreeNode()
        self.get_tree(nums, 0, len(nums)-1, root)
        return root


    def get_tree(self, nums, left, right, root):

        if left > right:
            return
        middle = (left + right) // 2
        root.val = nums[middle]
        root_left = TreeNode()
        root_right = TreeNode()
        if middle-1 >= left:
            root.left = root_left
            self.get_tree(nums, left, middle-1, root_left)
        if middle+1 <= right:
            root.right = root_right
            self.get_tree(nums, middle+1, right, root_right)
