#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#
from typing import List
# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [-1, -1]
        for n in nums:
            if nums[abs(n)-1]<0:
                res[0] = abs(n)
            else:
                nums[abs(n)-1] *= -1
        for i, n in enumerate(nums):
            if n>0:
                res[1] = i+1
        return res

# @lc code=end

nums = [1,2,2,4]
res = Solution().findErrorNums(nums)
print(res)