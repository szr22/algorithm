#
# @lc app=leetcode id=280 lang=python3
#
# [280] Wiggle Sort
#

from typing import List
# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        if len(nums)<=1:
            return
        for i in range(1, len(nums)):
            if (
                (i%2==1 and nums[i]<nums[i-1])
                or (i%2==0 and nums[i]>nums[i-1])
            ):
                nums[i-1], nums[i] = nums[i], nums[i-1]


# @lc code=end

nums = [1, 5, 1, 1, 6, 4]
# nums = [1,1,2,1,2,2,1]
# nums = [1,5,1,1,6,4]
# nums = [4,5,5,6]

Solution().wiggleSort(nums)
print(nums)