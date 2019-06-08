# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# Example:

# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]

from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.dfs(s, res, [])
        return res
    
    def dfs(self, s, res, cur):
        if len(cur) == 4 and not s:
            res.append('.'.join(cur))
            return
        for i in range(1, min(3, len(s))+1):
            nextStr = s[:i]
            if len(cur)<4 and self.isValid(nextStr):
                self.dfs(s[i:], res, cur+[nextStr])
            else:
                return
    
    def isValid(self, s):
        return s=='0' or 0<int(s)<=255

s = '25525511135'

res = Solution().restoreIpAddresses(s)
print(res)