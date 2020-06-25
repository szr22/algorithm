#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#
from typing import List
# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = {1: []}
        for num in sorted(nums):
            dp[num] = max([dp[k] for k in dp.keys() if not num%k], key=len)+[num]
            # print(dp)
        return max(dp.values(), key = len)

    def largestDivisibleSubsetStraight(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [0 for _ in range(len(nums))]
        parent = [0 for _ in range(len(nums))]
        res = []
        mx = 0
        mxIdx = 0

        for i in range(len(nums)-1, -1, -1):
            for j in range(i, len(nums)):
                if (nums[j]%nums[i]==0 and dp[i]<dp[j]+1):
                    dp[i] = dp[j]+1
                    parent[i] = j
                if mx<dp[i]:
                    mx = dp[i]
                    mxIdx = i
        for i in range(mx):
            res.append(nums[mxIdx])
            mxIdx = parent[mxIdx]
        return res
# @lc code=end

nums = [1,2,4,8, 3, 9, 27, 72, 81, 243]
res = Solution().largestDivisibleSubset(nums)
print(res)
