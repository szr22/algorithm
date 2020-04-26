#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold_pre, sold = 0, 0
        hold = -sys.maxsize

        for price in prices:
            sold_tmp = sold
            sold = max(sold, hold+price)
            hold = max(hold, sold_pre-price)
            sold_pre = sold_tmp
        return sold

# @lc code=end

