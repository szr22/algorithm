#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        nS = len(s)
        nP = len(p)
        if nS<nP or nP == 0:
            return []
        res = []
        cntP = Counter(p)
        for i in range(nS-nP+1):
            cur = s[i:i+nP]
            if cntP == Counter(cur):
                res.append(i)
        return res
# @lc code=end

