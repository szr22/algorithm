#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#
from typing import List
import functools
# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: (x[1], x[0]))
        print(pairs)
        stack = []
        for p in pairs:
            if not stack:
                stack.append(p)
            else:
                if p[0]>stack[-1][1]:
                    stack.append(p)
        return len(stack)

# @lc code=end

pairs = [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[0,3],[-5,3]]
res = Solution().findLongestChain(pairs)
print(res)
