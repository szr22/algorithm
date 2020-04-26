#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
from typing import List
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
        return dp[n]

    def wordBreakStraight(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True
        res = False
        for i in range(1,len(s)):
            if s[:i] in wordDict:
                res |= self.wordBreakStraight(s[i:], wordDict)
        return res

# @lc code=end

s = "applepenapple"
wordDict = ["apple", "pen"]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

s = "leetcode"
wordDict = ["leet", "code"]

res = Solution().wordBreak(s, wordDict)
print(res)