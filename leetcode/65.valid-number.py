#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        num = False
        numsAfterE = True
        dot = False
        exp = False
        sign = False
        n = len(s)

        for i in range(n):
            if s[i] == ' ':
                if i<n-1 and s[i+1]!=' ' and (num or dot or exp or sign):
                    return False
            elif s[i] in '+-':
                if i>0 and s[i-1] != 'e' and s[i-1] != ' ':
                    return False
                sign = True
            elif (s[i]) >= '0' and (s[i])<='9':
                num = True
                numsAfterE = True
            elif s[i] == '.':
                if dot or exp:
                    return False
                dot = True
            elif s[i] == 'e':
                if exp or not num:
                    return False
                exp = True
                numsAfterE = False
            else:
                return False
        return num and numsAfterE

# @lc code=end

