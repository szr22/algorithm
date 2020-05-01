#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#
from typing import List
# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        res = 1
        cur = 1
        # gap = nums[1]-nums[0]
        for i in range(1, len(nums)):
            # if nums[i]-nums[i-1] == gap:
            if nums[i]>nums[i-1]:
                cur += 1
            else:
                res = max(res, cur)
                cur = 1
                # gap = nums[i]-nums[i-1]
        return max(res, cur)
# @lc code=end

nums = [1,3,5,4,7]
nums = [2,2,2,2,2]
res = Solution().findLengthOfLCIS(nums)
print(res)