#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            memo[i][i] = 1
            for j in range(i+1, n):
                if s[i]==s[j]:
                    memo[i][j] = memo[i+1][j-1]+2
                else:
                    memo[i][j] = max(memo[i+1][j], memo[i][j-1])
        # print(memo)
        return memo[0][n-1]
# @lc code=end

s = "bbbab"
res = Solution().longestPalindromeSubseq(s)
print(res)