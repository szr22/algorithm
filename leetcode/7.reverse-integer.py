#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if x<0 else 1
        x = abs(x)
        while x:
            res *= 10
            res += x%10
            x //= 10
        res *= sign
        if res > 2**31-1 or res < -2**31:
            return 0
        return res
# @lc code=end

res = Solution().reverse(123456789)
print(res)