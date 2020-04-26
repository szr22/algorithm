#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#
from typing import List
import sys

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k >= n>>1:
            sold = 0
            hold = -sys.maxsize

            for price in prices:
                sold_tmp = sold
                sold = max(sold, hold+price)
                hold = max(hold, sold_tmp-price)
            return sold

        sold = [0] * (k+1)
        hold = [-sys.maxsize] * (k+1)
        for price in prices:
            for i in range(k, 0, -1):
                sold[i] = max(sold[i], hold[i]+price)
                hold[i] = max(hold[i], sold[i-1]-price)
            # print(sold)
            # print(hold)
        return sold[k]
# @lc code=end

k = 2
prices = [3,3,5,0,0,3,1,4]


res = Solution().maxProfit(k, prices)
print(res)