#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
from typing import List

# @lc code=start
class Node:
    def __init__(self, val, smaller):
        self.val = val
        self.smaller = smaller
        self.left = None
        self.right = None

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        t = []
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            left, right = 0, len(t)
            while left<right:
                mid = (left+right)//2
                if t[mid]>=nums[i]:
                    right = mid
                else:
                    left = mid+1
            res[i] = right
            t.insert(right, nums[i])
        return res

    def countSmallerTree(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        root = None
        for i in range(len(nums)-1, -1, -1):
            res[i], root = self.addNode(root, nums[i])
        return res

    def addNode(self, root, val):
        if not root:
            root = Node(val, 0)
            return 0, root
        if root.val > val:
            root.smaller += 1
            res, root.left = self.addNode(root.left, val)
            return res, root
        else:
            res, root.right = self.addNode(root.right, val)
            res += root.smaller
            if root.val<val:
                res += 1
            return res, root
# @lc code=end

