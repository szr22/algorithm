#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            sSorted = ('').join(sorted(s))
            if sSorted in dic:
                dic[sSorted].append(s)
            else:
                dic[sSorted] = [s]
        return dic.values()
# @lc code=end

