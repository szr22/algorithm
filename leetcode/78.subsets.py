#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
from typing import List
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        tmp = self.subsets(nums[1:])
        res = tmp.copy()
        for item in tmp:
            res.append([nums[0]]+item)
        return res
# @lc code=end

res = Solution().subsets([1,2,3])
print(res)