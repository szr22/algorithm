#
# @lc app=leetcode id=396 lang=python3
#
# [396] Rotate Function
#

# @lc code=start
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        f0 = 0
        total = 0
        n = len(A)
        for i in range(n):
            total += A[i]
            f0 += i*A[i]
        res = f0
        for i in range(1, n):
            f0 = f0 + total - n * A[n-i]
            res = max(res, f0)
        return res
# @lc code=end

