#
# @lc app=leetcode id=537 lang=python3
#
# [537] Complex Number Multiplication
#

# @lc code=start
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        idxA = a.rfind('+')
        a1 = int(a[:idxA])
        a2 = int(a[idxA+1:-1])
        idxB = b.rfind('+')
        b1 = int(b[:idxB])
        b2 = int(b[idxB+1:-1])
        r1 = a1*b1-a2*b2
        r2 = a1*b2+a2*b1
        return str(r1) + '+' + str(r2) + "i"
# @lc code=end

a ="78+-76i"
b = "-86+72i"

res = Solution().complexNumberMultiply(a,b)
print(res)