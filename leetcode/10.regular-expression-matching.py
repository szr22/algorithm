#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sLen, pLen = len(s), len(p)
        dp = [[False for _ in range(pLen+1)] for _ in range(sLen+1)]
        dp[0][0] = True

        for sIdx in range(sLen+1):
            for pIdx in range(1, pLen+1):
                if p[pIdx-1]=='*':
                    dp[sIdx][pIdx] = (
                        dp[sIdx][pIdx-2]
                        or (
                            sIdx>0
                            and pIdx>1
                            and dp[sIdx-1][pIdx]
                            and (
                                s[sIdx-1]==p[pIdx-2]
                                or p[pIdx-2]=='.'
                            )
                        )
                    )
                else:
                    dp[sIdx][pIdx] = (
                        sIdx>0
                        and dp[sIdx-1][pIdx-1]
                        and (
                            s[sIdx-1]==p[pIdx-1]
                            or p[pIdx-1]=='.'
                        )
                    )
        return dp[sLen][pLen]

    def isMatchRec(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if len(p) == 1:
            return len(s)==1 and (s[0]==p[0] or p[0]=='.')
        if p[1] != '*':
            if not s or (s[0]!=p[0] and p[0]!='.'):
                return False
            return self.isMatchRec(s[1:], p[1:])

        while s and (s[0]==p[0] or p[0]=='.'):
            if self.isMatchRec(s, p[2:]):
                return True
            s=s[1:]

        return self.isMatchRec(s, p[2:])

    def isMatchBad(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        if not p:
            return False
        if not s and (len(p)<2 or (len(p)>=2 and p[1]!='*')):
            return False
        i, j = 0, 0
        # handle * first
        if j+1<len(p) and p[j+1]=='*':
            if self.isMatchBad(s[i:], p[j+2:]):
                return True
            if s and s[i]!=p[i] and p[j]!='.':
                return self.isMatchBad(s[i:], p[j+2:])

            while i+1 <len(s) and (p[j]=='.' or s[i]==s[i+1]):
                if self.isMatchBad(s[i+1:], p[j+2:]):
                    return True
                i += 1

            if i==len(s):
                return j+2==len(p)
            else:
                return self.isMatchBad(s[i+1:], p[j+2:])

        if p and (s[i] == p[j] or p[j]=='.'):
            return self.isMatchBad(s[i+1:], p[j+1:])
        else:
            return False

# @lc code=end

s = "mississippi"
p = "mis*iss*ip*."

# s = "aab"
# p = "c*a*b"

# s = "ab"
# p = ".*"

# s = "aa"
# p = "a*"

s = "ab"
p = ".*a.*b"

s="ab"
p=".*c"

s="a"
p="ab*a"

# s="a"
# p=".*..a*"

# s = "aaa"
# p = "ab*a"

# s=""
# p="c*c*"

sol = Solution()
res = sol.isMatch(s, p)
print(res)