#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
from typing import List
# @lc code=start
class Solution:
    def __init__(self):
        self.hashMap = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if s in self.hashMap:
            return self.hashMap[s]
        if not s:
            return [""]
        res = []
        for word in wordDict:
            n = len(word)
            if s[:n] == word:
                remainList = self.wordBreak(s[n:], wordDict)
                for rem in remainList:
                    print(rem)
                    tmp = word
                    if rem:
                        tmp += ' ' + rem
                    res.append(tmp)
        self.hashMap[s] = res
        return res

    def wordBreakDfs(self, s: str, wordDict: List[str]) -> List[str]:
        cur = []
        res = []
        self.helperDfs(s, cur, res, wordDict)
        return res

    def helperDfs(self, s, cur, res, wordDict):
        if len(s) == 0:
            res.append(cur)
            return
        for i in range(1, len(s)+1):
            subS = s[:i]
            if subS in wordDict:
                self.helperDfs(s[i:], cur+[subS], res, wordDict)


# @lc code=end

s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

res = Solution().wordBreak(s, wordDict)
print(res)