#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x==y:
            return 0
        else:
            z = x^y
            z = bin(z)
            return z.count('1')
# @lc code=end

