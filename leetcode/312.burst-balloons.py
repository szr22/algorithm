#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
        for size in range(1, n+1):
            for left in range(1, n-size+2):
                right = left+size-1
                for idx in range(left, right+1):
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left-1]*nums[idx]*nums[right+1]+dp[left][idx-1]+dp[idx+1][right]
                    )
        return dp[1][n]
# @lc code=end

