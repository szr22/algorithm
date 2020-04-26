#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold = [0]*n
        sold = [0]*n
        hold = -prices[0]
        for i in range(1, n):
            hold[i] = max(hold[i-1], sold[i-1]-prices[i])
            sold[i] = max(sold[i-1], hold[i-1]+prices[i]-fee)
            print(sold)
            print(hold)
        return sold[-1]

# @lc code=end

prices = [1, 3, 2, 8, 4, 9]
fee = 2

res = Solution().maxProfit(prices, fee)
print(res)