#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
from typing import List
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0:
            return False
        target = total//2
        dp = [False for _ in range(target+1)]
        dp[0] = True
        for num in nums:
            for i in range(target, num-1, -1):
                print(i)
                dp[i] |= dp[i-num]
            print(dp)

        return dp[target]


# @lc code=end

nums = [1, 5, 6, 3, 2, 5]
# nums = [1, 2, 3, 5]
res = Solution().canPartition(nums)
print(res)