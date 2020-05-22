#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def __init__(self):
        self.romabNumTable = [
            ('M', 1000),
            ('D', 500),
            ('C', 100),
            ('L', 50),
            ('X', 10),
            ('V', 5),
            ('I', 1),
        ]
    def intToRoman(self, num: int) -> str:
        res = ''
        for i in range(len(self.romabNumTable)):
            div, mod = divmod(num, self.romabNumTable[i][1])
            if div == 4:
                res = self.handleDup(res, i)
            else:
                res += div*self.romabNumTable[i][0]
            num = mod
        return res

    def handleDup(self, res, i):
        # print(self.romabNumTable[i-1][0],res[-1])
        if res and self.romabNumTable[i-1][0]==res[-1]:
            return res[:-1] + self.romabNumTable[i][0] + self.romabNumTable[i-2][0]
        else:
            return res + self.romabNumTable[i][0] + self.romabNumTable[i-1][0]

# @lc code=end

res = Solution().intToRoman(0)
print(res)