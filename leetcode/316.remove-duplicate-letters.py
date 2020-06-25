#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#
from collections import defaultdict
# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        chCnt = defaultdict(int)
        visited = {}
        res = ["0"]
        for c in s:
            chCnt[c] += 1
        for c in s:
            chCnt[c] -= 1
            if c in visited and visited[c]==1:
                continue
            while c < res[-1] and chCnt[res[-1]]:
                visited[res[-1]] = 0
                res.pop()
            res.append(c)
            visited[c] = 1
            # print(res)
        return "".join(res[1:])

# @lc code=end

s = "bcabc"
s = "cbacdcbc"
res = Solution().removeDuplicateLetters(s)
print(res)