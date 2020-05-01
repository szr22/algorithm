#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
from typing import List
import sys
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold1, hold2 = -sys.maxsize, -sys.maxsize
        sold1, sold2 = 0, 0
        for price in prices:
            sold2 = max(sold2, hold2+price)
            hold2 = max(hold2, sold1-price)
            sold1 = max(sold1, hold1+price)
            hold1 = max(hold1, -price)
        return sold2

# @lc code=end

