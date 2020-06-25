#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        dp = []
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        for i in range(len(envelopes)):
            left, right = 0, len(dp)
            t = envelopes[i][1]
            while left<right:
                mid = (left+right)//2
                if dp[mid]<t:
                    left = mid+1
                else:
                    right = mid
                    
            if right>=len(dp):
                dp.append(t)
            else:
                dp[right] = t
        return len(dp)
# @lc code=end

