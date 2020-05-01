#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
from typing import List
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
            # print(nums)
        return nums

# @lc code=end
nums = [7,0, 0,1,0,3,12, 0, 9]
res = Solution().moveZeroes(nums)
print(res)

class Solution2:
    def moveZeroes(self, nums: List[int]):
        left, right = 0, 0
        for right in range(len(nums)):
            print(nums)
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

    def moveNeg(self, nums):
        left, right = 0, 0
        while right < len(nums):
            if nums[right] < 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        right = left
        while right < len(nums):
            if nums[right] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
            # print(nums)

nums = [0, 0,1,0,3,12, -1, -1]
res = Solution2().moveNeg(nums)