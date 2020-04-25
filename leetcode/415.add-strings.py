#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len1, len2 = len(num1), len(num2)
        maxLen = max(len1, len2)
        i = 0
        res = ''
        carryOn = 0
        while i < maxLen:
            curPos = -1-i
            tmp = carryOn
            if i<len1:
                tmp += int(num1[curPos])
            if i<len2:
                tmp += int(num2[curPos])

            carryOn = tmp//10
            tmp %= 10
            res = str(tmp)+res
            i+=1

        if carryOn>0:
            res = '1'+res
        return res

    def addStringsBetter(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        carry, res = 0 , ''
        while num1 or num2 or carry:
            if num1:
                carry += int(num1.pop())
            if num2:
                carry += int(num2.pop())
            res += str( carry % 10 )
            carry = carry // 10
        return res[::-1]

# @lc code=end

num1 = '1999999999'
num2 = '3'

res = Solution().addStrings(num1, num2)
print(res)