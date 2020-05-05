#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = {}
        for coin in coins:
            dp[coin] = 1
        for i in range(amount+1):
            if i in dp:
                continue
            for coin in coins:
                if i-coin in dp:
                    if i not in dp:
                        dp[i] = dp[i-coin]+1
                    else:
                        dp[i] = min(dp[i], dp[i-coin]+1)
        if amount in dp:
            return dp[amount]
        return -1

# @lc code=end

