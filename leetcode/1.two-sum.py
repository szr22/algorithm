#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        for idx, num in enumerate(nums):
            if target-num in hashMap:
                return [hashMap[target-num], idx]
            else:
                hashMap[num] = idx
        return []



# @lc code=end

nums = [2, 7, 11, 15]
target = 9
res = Solution().twoSum(nums, target)
print(res)