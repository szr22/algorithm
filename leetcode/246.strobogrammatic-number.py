"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
"""

class Solution:
    def __init__(self):
        self.rotMap = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }

    def isStrobogrammatic(self, num: str) -> bool:
        n = len(num)
        mid = (n-1)//2
        for i in range(mid):
            if num[i] in self.rotMap:
                if num[n-i-1] != self.rotMap[num[i]]:
                    return False
            else:
                return False
        return True


num = '962'
num = '88'

num = '69'

res = Solution().isStrobogrammatic(num)
print(res)