#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        res = 10
        cnt = 9
        for i in range(2, n+1):
            cnt *= (11-i)
            res += cnt
        return res
# @lc code=end

