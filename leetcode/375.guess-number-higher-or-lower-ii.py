#
# @lc app=leetcode id=375 lang=python3
#
# [375] Guess Number Higher or Lower II
#

# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(2, n+1):
            for j in range(i-1, -1, -1):
                globalMin = sys.maxsize
                for k in range(j+1, i):
                    localMax = k+max(dp[j][k-1], dp[k+1][i])
                    globalMin = min(globalMin, localMax)
                dp[j][i] = j if j+1==i else globalMin
        return dp[1][n]

# @lc code=end

