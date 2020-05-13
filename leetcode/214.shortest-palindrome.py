#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i = 0
        n = len(s)
        for j in range(n-1, -1, -1):
            if s[i]==s[j]:
                i+=1
        if i==n:
            return s
        rem = s[i:][::-1]
        return rem +  self.shortestPalindrome(s[:i]) + s[i:]



# @lc code=end

