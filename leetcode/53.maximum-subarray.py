#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List
import sys
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, res = -sys.maxsize, -sys.maxsize
        for num in nums:
            cur = max(cur+num, num)
            res = max(cur, res)
        return res
# @lc code=end

nums = [-2,1,-3,4,-1,2,1,-5,4,3]
res = Solution().maxSubArray(nums)
print(res)