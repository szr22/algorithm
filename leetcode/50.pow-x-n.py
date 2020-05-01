#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        i = abs(n)
        while i != 0:
            if i%2 != 0:
                res *= x
            x *=x
            i //= 2
            # print(i)
        if n<0:
            return 1/res
        else:
            return res


# @lc code=end

res = Solution().myPow(2.000, -2)
print(res)
