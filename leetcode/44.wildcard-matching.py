#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatchIter(self, s: str, p: str) -> bool:
        i = 0
        j = 0
        # track position of star
        i_star = -1
        j_star = -1
        s_len = len(s)
        p_len = len(p)
        # check s to the end
        while i<s_len:
            print(i, j, i_star, j_star)
            if j<p_len and (s[i]==p[j] or p[j]=='?'):
                i+=1
                j+=1
            elif j<p_len and p[j]=='*':
                i_star = i
                j_star = j
                j += 1
            elif i_star>=0:
                i_star += 1
                i = i_star
                j = j_star+1
            else:
                return False
        # check rest * in p
        while j<p_len and p[j] == '*':
            j+=1
        return j==p_len

    def isMatch(self, s:str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        dp = [[False for _ in range(p_len+1)] for _ in range(s_len+1)]
        dp[0][0] = True
        for i in range(1, p_len+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-1]

        for s_idx in range(1, s_len+1):
            for p_idx in range(1, p_len+1):
                if p[p_idx-1] == '*':
                    dp[s_idx][p_idx] = dp[s_idx-1][p_idx] or dp[s_idx][p_idx-1]
                else:
                    dp[s_idx][p_idx] = (
                        (s[s_idx-1]==p[p_idx-1] or p[p_idx-1] == '?')
                        and dp[s_idx-1][p_idx-1]
                    )
        return dp[s_len][p_len]
# @lc code=end

s = "adceb"
p = "*a*b"

s = "acdcb"
p = "a*c?b"

s = "adcfebafebd"
p = "adc*a**d**"

s = "cfaeba"
p = "c*a*"

s = "aa"
p = "a"

res = Solution().isMatch(s, p)
print(res)