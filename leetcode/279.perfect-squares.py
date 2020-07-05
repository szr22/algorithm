#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
from math import sqrt
import sys

# @lc code=start
class Solution:
    def numSquaresMath(self, n: int) -> int:
        while n%4==0:
            n //= 4
        if n%8 == 7:
            return 4
        a = 0
        while a*a<=n:
            b = int(sqrt(n-a*a))
            if a*a+b*b == n:
                if a>0 and b>0:
                    return 2

                return 1
            a += 1
        return 3

    def numSquaresTLE(self, n: int) -> int:
        dp = [sys.maxsize] * (n+1)
        dp[0] = 0
        for i in range(0, n+1):
            j = 1
            while i+j*j <= n:
                dp[i+j*j] = min(dp[i+j*j], dp[i]+1)
                j += 1
        return dp[-1]

    def numSquares(self, n: int) -> int:
        dp = [0]
        while len(dp) <= n:
            m = len(dp)
            val = sys.maxsize
            i = 1
            while i*i <= m:
                val = min(val, dp[m-i*i]+1)
                i += 1
            dp.append(val)
        return dp[-1]

# @lc code=end

res = Solution().numSquares(6024)
print(res)