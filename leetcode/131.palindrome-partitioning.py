#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.helper(s, 0, [])
        return self.res

    def helper(self, s, start, cur):
        if start == len(s):
            self.res.append(cur.copy())
        for i in range(start, len(s)):
            if not self.isPalindrome(s, start, i):
                continue
            cur.append(s[start: i+1])
            self.helper(s, i+1, cur)
            cur.pop()

    def isPalindrome(self, s, start, end):
        while start<end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
# @lc code=end

