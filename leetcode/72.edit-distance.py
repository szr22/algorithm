#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
from functools import lru_cache
# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        len1, len2 = len(word1), len(word2)
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        for i in range(1, len1+1):
            dp[i][0] = i
        for i in range(1, len2+1):
            dp[0][i] = i

        for i1 in range(1, len1+1):
            for i2 in range(1, len2+1):
                if word1[i1-1]==word2[i2-1]:
                    dp[i1][i2] = dp[i1-1][i2-1]
                else:
                    dp[i1][i2] = 1 + min(
                        dp[i1-1][i2],
                        dp[i1][i2-1],
                        dp[i1-1][i2-1]
                    )
        # print(dp)
        return dp[len1][len2]

    @lru_cache(None)
    def editDistanceRec(self, str1, str2):
        m, n = len(str1), len(str2)
        if m == 0 or n==0:
            return m+n

        if str1[m-1]== str2[n-1]:
            return self.editDistanceRec(str1[:m-1], str2[:n-1])

        return min(
                    self.editDistanceRec(str1, str2[:n-1]),    # Insert
                    self.editDistanceRec(str1[:m-1], str2),    # Remove
                    self.editDistanceRec(str1[:m-1], str2[:n-1])    # Replace
                ) + 1

# @lc code=end

word1 = "horse"
word2 = "ros"

word1 = "intention"
word2 = "execution"

word1 = "pneumonoultramicroscopicsilicovolcanoconiosis"
word2 = "ultramicroscopically"

word1 = "distance"
word2 = "springbok"

res = Solution().minDistance(word1, word2)
print(res)