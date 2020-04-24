#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def __init__(self):
        self.romanIntMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
    def romanToInt(self, s: str) -> int:
        res = 0
        pre = None
        for i in range(len(s)-1, -1, -1):
            char = s[i]
            tmp = self.romanIntMap[char]
            if pre and self.romanIntMap[pre]>self.romanIntMap[char]:
                tmp = -tmp
            res += tmp
            pre = char
        return res

# @lc code=end

