#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        while start<end:
            if s[start] != s[end]:
                return (
                    self.isValid(s, start, end-1)
                    or self.isValid(s, start+1, end)
                )
            start+=1
            end-=1
        return True

    def isValid(self, s, start, end):
        while start<end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True

# @lc code=end

