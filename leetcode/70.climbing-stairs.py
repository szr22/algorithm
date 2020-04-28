#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        preTwo = 1
        preOne = 2
        for _ in range(2, n):
            cur = preOne+preTwo
            preTwo = preOne
            preOne = cur
        return preOne

    def climbStairsThree(self, n):
        if n<3:
            return n
        if n == 3:
            return 4

        preThree = 1
        preTwo = 2
        preOne = 4
        for _ in range(4, n):
            cur = preThree + preTwo + preOne
            preThree = preTwo
            preTwo = PreOne
            PreOne = cur
        return preOne

# @lc code=end


