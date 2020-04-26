#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        len1, len2 = len(text1), len(text2)
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        for i1 in range(1, len1+1):
            for i2 in range(1, len2+1):
                if text1[i1-1]==text2[i2-1]:
                    dp[i1][i2] = dp[i1-1][i2-1] + 1
                else:
                    dp[i1][i2] = max(dp[i1-1][i2], dp[i1][i2-1])
        return dp[len1][len2]

    def longestCommonSubsequenceRec(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        return self.lcsRec(text1, text2, 0, 0)

    def lcsRec(self, text1, text2, i1, i2):
        print(i1, i2)
        if i1 == len(text1) or i2 == len(text2):
            return 0

        if text1[i1] == text2[i2]:
            return self.lcsRec(text1, text2, i1+1, i2+1) + 1
        else:
            return max(self.lcsRec(text1, text2, i1+1, i2), self.lcsRec(text1, text2, i1, i2+1))

# @lc code=end

text1 = "abcde"
text2 = "ace"

text1 = "pmjghexybyrgzczy"
text2 = "hafcdqbgncrcbihkd"
res = Solution().longestCommonSubsequenceRec(text1, text2)
print(res)