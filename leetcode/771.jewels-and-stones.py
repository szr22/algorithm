#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#
from collections import Counter
# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        sCounter = Counter(S)
        res = 0
        for j in J:
            if j in sCounter:
                res+=sCounter[j]
        return res
# @lc code=end

J = "aA"
S = "aAAbbbb"
res = Solution().numJewelsInStones(J, S)
print(res)