#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
class Solution:
    def __init__(self):
        self.dictLessTwenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.dictTens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.dictMoreHundred = ["Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:

        res = self.numberToHundred(num%1000)
        for i in range(3):
            num //= 1000
            if num % 1000 == 0:
                res
            else:
                res = self.numberToHundred(num % 1000) + ' ' + self.dictMoreHundred[i] + ' ' + res
        while res and res[-1] == ' ':
            res = res[:-1]

        if not res:
            return 'Zero'
        else:
            return res

    def numberToHundred(self, num: int) -> str:
        res = ''
        hundredNum = num // 100
        hundredRemainderNum = num % 100
        tenRemainderNum = num % 10

        if hundredRemainderNum<20:
            res = self.dictLessTwenty[hundredRemainderNum]
        else:
            res = self.dictTens[hundredRemainderNum//10]
            if tenRemainderNum > 0:
                res += ' ' + self.dictLessTwenty[tenRemainderNum]
        if hundredNum>0:
            if hundredRemainderNum>0:
                res = ' ' + res
            res = self.dictLessTwenty[hundredNum] + ' Hundred' + res

        return res

# @lc code=end

num = 1234567891
num = 1051
res = Solution().numberToWords(num)
print(res)