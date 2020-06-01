#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#
from typing import List
import sys
# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1 for _ in range(n)]
        idx = [0 for _ in range(len(primes))]
        for i in range(1, n):
            dp[i] = sys.maxsize
            for j in range(len(primes)):
                dp[i] = min(dp[i], dp[idx[j]]*primes[j])
            for j in range(len(primes)):
                if dp[i] == dp[idx[j]]*primes[j]:
                    idx[j] += 1
            # print(idx)
        return dp[-1]
# @lc code=end

res = Solution().nthSuperUglyNumber(12, [2,7,13,19])
print(res)