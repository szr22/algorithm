#
# @lc app=leetcode id=686 lang=python3
#
# [686] Repeated String Match
#

# @lc code=start
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        len_b = len(B)
        cnt = 1
        ext_a = A
        while len(ext_a) < len_b:
            ext_a += A
            cnt += 1
        if B in ext_a:
            return cnt
        ext_a += A
        cnt += 1
        return cnt if B in ext_a else -1

# @lc code=end

