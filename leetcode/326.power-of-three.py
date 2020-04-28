#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#
from math import log10
# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False

        while n and n%3==0:
            n //= 3

        return n == 1

    def isPowerOfThreeMath(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

    def isPowerOfThreeLog(self, n: int) -> bool:

        return (n > 0 and int(log10(n) // log10(3)) - log10(n) // log10(3) == 0)

# @lc code=end

print(Solution().isPowerOfThree(-2147483648))