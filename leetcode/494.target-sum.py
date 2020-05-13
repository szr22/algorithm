#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from collections import defaultdict
# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0]=1
        for i in range(n):
            for total, cnt in dp[i].items():
                dp[i+1][total+nums[i]] += cnt
                dp[i+1][total-nums[i]] += cnt
        return dp[-1][S]

    def findTargetSumWaysTLE(self, nums: List[int], S: int) -> int:
        self.res = 0
        self.helper(nums, S, 0)
        return self.res

    def helper(self, nums, S, pos):
        if pos>=len(nums):
            if S==0:
                self.res += 1
            return self.res
        self.helper(nums, S-nums[pos], pos+1)
        self.helper(nums, S+nums[pos], pos+1)

# @lc code=end

