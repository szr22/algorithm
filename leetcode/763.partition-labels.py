#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

from collections import defaultdict, OrderedDict
import sys
from typing import List

# @lc code=start
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        c_end = defaultdict(list)
        for i, c in enumerate(S):
            if c not in c_end:
                c_end[c] = i
            else:
                c_end[c] = max(c_end[c], i)
        start = 0
        res = []
        while start < len(S):
            end  = c_end[S[start]]
            idx = start+1
            while idx < end:
                end = max(c_end[S[idx]], end)
                idx += 1
            res.append(end+1-start)
            start = end+1
        return res

    def partitionLabels_faster(self, S: str) -> List[int]:
        keys = list(OrderedDict.fromkeys(S))

        first =[S.index(i) for i in keys]
        S = S[::-1]
        last = [len(S) - S.index(i) -1 for i in keys]

        result, start, end =[], first[0], last[0]

        for i in range(1,len(first)):
            if first[i]< end:
                end = max(end,last[i])
            else:
                result.append(end-start+1)
                start, end = first[i], last[i]

        result.append(end-start+1)
        return result

# @lc code=end

S = "ababcbacadefegadehijhklij"
res = Solution().partitionLabels(S)
print(res)