#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import List

# @lc code=start
class Solution:
    def __init__(self):
        self.letMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = ['']
        for d in digits:
            tmp = []
            while res:
                item = res.pop()
                for char in self.letMap[d]:
                    tmp.append(item + char)
            res = tmp
        return res

# @lc code=end

d = "28736"
res = Solution().letterCombinations(d)
print(res)