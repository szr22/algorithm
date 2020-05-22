#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cSet = set()
        start = 0
        end = 0
        res = 0
        for i, c in enumerate(s):

            while c in cSet:
                cSet.remove(s[start])
                start += 1
            cSet.add(c)
            end = i
            res = max(res, end-start+1)
        return res

# @lc code=end

