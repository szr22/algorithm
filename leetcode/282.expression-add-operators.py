#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#
from typing import List
# @lc code=start
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        self.helper(num, target, 0, 0, '', res)
        return res

    def helper(self, num, target, diff, curNum, out, res):
        if len(num)==0 and curNum == target:
            res.append(out)
            print(out)
            return
        for i in range(1, len(num)+1):
            cur = num[:i]
            if len(cur)>1 and cur[0]=='0':
                return
            next = num[i:]
            if len(out)>0:
                self.helper(next, target, int(cur), curNum+int(cur), out+'+'+cur, res)
                self.helper(next, target, -int(cur), curNum-int(cur), out+'-'+cur, res)
                self.helper(next, target, diff*int(cur), (curNum-diff)+diff*int(cur), out+'*'+cur, res)
            else:
                self.helper(next, target, int(cur), int(cur), cur, res)

# @lc code=end

num = "123"
target = 6

res = Solution().addOperators(num, target)
print(res)