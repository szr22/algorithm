#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        fst = -float('inf')
        scd = -float('inf')
        thd = -float('inf')
        for num in nums:
            if num>fst:
                thd = scd
                scd = fst
                fst = num
            elif num>scd and num<fst:
                thd = scd
                scd = num
            elif num>thd and num<scd:
                thd = num
        if thd == -float('inf'):
            return fst
        else:
            return thd
# @lc code=end

