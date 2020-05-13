#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstringsRec(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        self.res = 0
        for i in range(n):
            self.helper(s, i, i)
            self.helper(s, i, i+1)
        return self.res

    def helper(self, s, i, j):
        while i>=0 and j<len(s) and s[i]==s[j]:
            i -= 1
            j += 1
            self.res += 1

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = (s[i]==s[j]) and (j-i<=2 or dp[i+1][j-1])
                if dp[i][j]:
                    res += 1
        return res
# @lc code=end

