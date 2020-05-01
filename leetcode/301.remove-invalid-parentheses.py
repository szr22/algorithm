#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#
from typing import List
# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        visited = set([s])
        queue = [s]
        found = False
        while queue:
            print(queue)
            cur = queue.pop(0)
            if self.isValid(cur):
                res.append(cur)
                found = True
            if not found:
                for i in range(len(cur)):
                    if cur[i] in '()':
                        tmp = cur[:i]+cur[i+1:]
                        if tmp not in visited:
                            queue.append(tmp)
                            visited.add(tmp)

        return res

    def removeInvalidParenthesesStraight(self, s: str) -> List[str]:
        res = []
        cur = set([s])
        while cur:
            nxt = set()
            for subS in cur:
                if self.isValid(subS):
                    res.append(subS)
                if not res:
                    for i in range(len(subS)):
                        if subS[i] in '()':
                            nxt.add(subS[:i]+subS[i+1:])
            if res:
                return res
            cur = nxt
        return res

    def isValid(self, s):
        cnt = 0
        for c in s:
            if c=='(':
                cnt+=1
            if c==')':
                cnt-=1
            if cnt<0:
                return False
        return cnt == 0


# @lc code=end

s = "(a)())()"

res = Solution().removeInvalidParentheses(s)
print(res)