#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        n = len(s)
        self.maxLen = 0
        self.start = 0
        for i in range(n):
            self.searchPalindrome(s, i, i)
            self.searchPalindrome(s, i, i+1)
        return s[self.start:self.start+self.maxLen]

    def searchPalindrome(self, s, left, right):
        while (left>=0 and right<len(s) and s[left]==s[right]):
            left-=1
            right+=1
        if self.maxLen<right-left-1:
            self.start = left+1
            self.maxLen = right-left-1

    def longestPalindromeDp(self, s: str) -> str:
        if len(s) < 2:
            return s
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        start = 0
        maxLen = 1

        for i in range(n):
            dp[i][i] = 1
            for j in range(i):
                dp[j][i] = s[i]==s[j] and (i-j<2 or dp[j+1][i-1]>0)
                if dp[j][i] and maxLen<i-j+1:
                    maxLen = i-j+1
                    start = j
        return s[start:start+maxLen]

    def longestPalindromeManacher(self, s: str) -> str:
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
# @lc code=end

