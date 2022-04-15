#
# @lc app=leetcode id=600 lang=python3
#
# [600] Non-negative Integers without Consecutive Ones
#

# @lc code=start
class Solution:
    def findIntegers(self, n: int) -> int:
        f = [1, 2]
        for i in range(2, 30):
            f.append(f[-1]+f[-2])

        res, prv_bit = 0, 0
        prv_bit = 0

        for i in reversed(range(30)):
            if n & (1 << i): # is the ith bit set?
                res += f[i]
                if prv_bit:
                    res -= 1
                    break
                prv_bit = 1
            else:
                prv_bit = 0
        return res+1
# @lc code=end

