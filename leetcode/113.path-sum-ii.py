#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        def dfs(head, cur_path, target):
            if not head:
                return
            cur_path.append(head.val)
            target -= head.val

            if target == 0 and not head.right and not head.left:
                res.append(cur_path.copy())
            dfs(head.left, cur_path, target)
            dfs(head.right, cur_path, target)
            cur_path.pop()

        dfs(root, [], targetSum)
        return res

# @lc code=end

