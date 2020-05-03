#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        idx1, idx2 = len(a)-1, len(b)-1
        res = ''
        car = 0
        while idx1>=0 and idx2>=0:
            tmp = int(a[idx1])+int(b[idx2])+car
            car = tmp//2
            res = str(tmp%2)+res
            idx1 -= 1
            idx2 -= 1
        while idx1>=0:
            tmp = int(a[idx1])+car
            car = tmp//2
            res = str(tmp%2)+res
            idx1 -= 1
        while idx2>=0:
            tmp = int(b[idx2])+car
            car = tmp//2
            res = str(tmp%2)+res
            idx2 -= 1
        if car:
            return '1'+res
        return res
# @lc code=end

