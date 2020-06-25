#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
from math import factorial
# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factor = factorial(n-1)
        numsLeft = list(range(1, n+1))
        k -= 1
        res = []
        for i in range(n-1, 0, -1):
            # print(factor)
            idx = k//factor
            res += str(numsLeft[idx])
            numsLeft.pop(idx)
            k %= factor
            factor //= i
        res += str(numsLeft[0])
        return ''.join(res)

# @lc code=end
n, k = 4, 9
res = Solution().getPermutation(n, k)
print(res)