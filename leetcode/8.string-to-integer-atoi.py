#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0
        INT_MAX=2**31-1
        INT_MIN=-2**31
        sign = 1
        base = 0
        i = 0
        n = len(str)
        while i<n and str[i]==' ':
            i+=1
        if i<n and str[i] in '+-':
            sign = 1 if str[i]=='+' else -1
            i+=1
        while i<n and str[i]>='0' and str[i]<='9':
            if base>INT_MAX//10 or (base == INT_MAX//10 and int(str[i])>7):
                return INT_MAX if sign==1 else INT_MIN
            base = 10*base+int(str[i])
            i+=1
        return base*sign
# @lc code=end

