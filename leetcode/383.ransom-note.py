#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
from collections import defaultdict
# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = defaultdict(int)
        for c in magazine:
            m[c]+=1

        for c in ransomNote:
            if c not in m:
                return False
            m[c] -= 1
            if m[c] < 0:
                return False

        return True

# @lc code=end

ransomNote = "aa"
magazine = "aab"
res = Solution().canConstruct(ransomNote, magazine)
print(res)