#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        n = len(s)
        for i in range(n//2,0,-1):
            if n % i == 0:
                # print(i)
                cnt = n//i
                tmp = s[:i]*cnt
                if tmp==s:
                    return True

        return False

# @lc code=end
s = "babbabbabbabbab"
res = Solution().repeatedSubstringPattern(s)
print(res)