#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#

# @lc code=start
class Solution:
    def minDistanceDP(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        n1, n2 = len(word1), len(word2)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

        for i in range(n1+1):
            dp[i][0] = i

        for i in range(n2+1):
            dp[0][i] = i

        for i1 in range(1, n1+1):
            for i2 in range(1, n2+1):
                if word1[i1-1] == word2[i2-1]:
                    dp[i1][i2] = dp[i1-1][i2-1]
                else:
                    dp[i1][i2] = min(dp[i1-1][i2], dp[i1][i2-1])+1

        return dp[n1][n2]

    def minDistance(self, word1: str, word2: str) -> int:
        return len(word1)+len(word2)-self.LongestCommonSubsequence(word1, word2)*2

    def LongestCommonSubsequence(self, word1, word2):
        if len(word1)>len(word2):
            word1, word2 = word2, word1

        n1, n2 = len(word1), len(word2)
        pre = [0 for _ in range(n1+1)]
        cur = pre.copy()
        for i2 in range(1, n2+1):
            for i1 in range(1, n1+1):
                if word1[i1-1]==word2[i2-1]:
                    cur[i1] = pre[i1-1]+1
                else:
                    cur[i1] = max(pre[i1], cur[i1-1])
            pre, cur = cur, pre

        return pre[-1]


# @lc code=end

