#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        sum = 0
        res = 0
        hash_map = defaultdict(int)
        for i in range(len(nums)):
            sum += nums[i]
            if sum == k:
                res += 1
            if sum-k in hash_map:
                res += hash_map[sum-k]
            hash_map[sum] += 1
        return res

    def subarraySumElt(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        res = 0
        if nums[0] == k:
            res += 1
        for i in range(1, n):
            nums[i] += nums[i-1]
            if nums[i] == k:
                res += 1

        for i in range(n-1):
            for j in range(i+1,n):
                if nums[j]-nums[i] == k:
                    res += 1
        return res
# @lc code=end

nums = [-92,-63,75,-86,-58,22,31,-16,-66,-67,420]
k = 100

nums = [1]
k = 2

res = Solution().subarraySum(nums, k)
print(res)