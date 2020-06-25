#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#
from collections import defaultdict
# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        m = defaultdict(int)
        for c in s:
            m[c] += 1
        for c in t:
            m[c] -= 1
            if m[c]<0:
                return c

# @lc code=end

