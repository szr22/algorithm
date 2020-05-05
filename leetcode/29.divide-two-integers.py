#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def __init__(self):
        self.INT_MAX = 2147483647
        self.INT_MIN = -2147483648

    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == self.INT_MIN and divisor == -1:
            return self.INT_MAX

        sign = 1
        if (divisor<0) ^ (dividend<0) == True:
            sign = -1

        num = abs(dividend)
        den = abs(divisor)
        res = 0

        if den == 1:
            return num if sign==1 else -num

        while num>=den:
            tmp = den
            p = 1
            while num >= tmp<<1:
                tmp <<= 1
                p <<= 1
            res += p
            num -= tmp

        return res if sign==1 else -res
# @lc code=end

# 7 \n -3