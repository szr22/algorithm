#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#
from typing import List

# @lc code=start
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = set()
        hashmap = {}
        for i, w in enumerate(words):
            hashmap[w] = i

        for idx, word in enumerate(words):
            if word and self.isValid(word) and '' in hashmap:
                res.add((idx, hashmap['']))
                res.add((hashmap[''], idx))
            rWord = word[::-1]
            if word and rWord in hashmap and idx != hashmap[rWord]:
                res.add((idx, hashmap[rWord]))
                res.add((hashmap[rWord], idx))

            for x in range(1, len(word)):
                left, right = word[:x], word[x:]
                rleft, rright = left[::-1], right[::-1]
                if self.isValid(left) and rright in hashmap:
                    res.add((hashmap[rright], idx))
                if self.isValid(right) and rleft in hashmap:
                    res.add((idx, hashmap[rleft]))

        return list(res)

    def isValid(self, s):
        start = 0
        end = len(s)-1
        while start<end:
            if s[start]==s[end]:
                start+=1
                end-=1
            else:
                return False
        return True
# @lc code=end

words = ["abcd", "dcba", "lls", "s", "sssll"]
words = ["a",""]
words = ["a","abc","aba",""]
words = ["a","b","c","ab","ac","aa"]
res = Solution().palindromePairs(words)
print(res)