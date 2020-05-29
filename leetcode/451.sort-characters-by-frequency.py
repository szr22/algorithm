#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        cntDict = Counter(s)
        res = ''
        for char, cnt in (sorted(cntDict.items(), key = lambda item: item[1], reverse=True)):
            res += char*cnt
        return res
# @lc code=end

