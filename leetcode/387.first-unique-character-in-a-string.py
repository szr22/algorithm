#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for i, c in enumerate(s):
            if c in d:
                d[c] = -1
            else:
                d[c] = i
        res = float('inf')
        for v in d.values():
            if v!=-1:
                res = min(res, v)
        if res == float('inf'):
            return -1
        else:
            return res
# @lc code=end

