#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#
from typing import List
# @lc code=start
class Solution:
    def wiggleSortAdv(self, nums: List[int]) -> None:
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        mid = (len(nums)+1) // 2
        left, right = nums[:mid], nums[mid:]
        nums[::2] = left[::-1]
        nums[1::2] = right[::-1]
 
# @lc code=end

nums = [1, 5, 1, 1, 6, 4]
nums = [1,1,2,1,2,2,1]
nums = [1,5,1,1,6,4]
nums = [4,5,5,6]

Solution().wiggleSort(nums)
print(nums)