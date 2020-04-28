#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        s1 = 1 if numerator>=0 else -1
        s2 = 1 if denominator>=0 else -1
        num = abs(numerator)
        den = abs(denominator)
        div, mod = divmod(num, den)
        res = str(div)
        if s1*s2<0 and (div>0 or mod>0):
            res = '-'+res
        if mod == 0:
            return res
        res += '.'
        modDict = dict()
        modDict[mod] = len(res)
        while mod:
            mod *= 10
            div, mod = divmod(mod, den)
            res += str(div)
            if mod in modDict:
                idx = modDict[mod]
                res = res[:idx] + '(' + res[idx:] + ')'
                break
            else:
                modDict[mod] = len(res)
        return res

# @lc code=end


res = Solution().fractionToDecimal(1,115)
print(res)