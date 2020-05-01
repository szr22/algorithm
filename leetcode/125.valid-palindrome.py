#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
import re
import string
# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = re.escape(string.punctuation)
        s = re.sub(r'['+chars+' ]', '',s).lower()
        n = len(s)
        mid = n//2
        for i in range(mid):
            if s[i]!=s[n-1-i]:
                return False
        return True


# @lc code=end

s = "A man, a plan, a canal: Panama"
res = Solution().isPalindrome(s)
print(res)