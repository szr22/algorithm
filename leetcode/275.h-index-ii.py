#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        n = len(citations)
        lo, hi = 0, len(citations)-1
        while lo<hi:
            mid = (lo+hi)//2
            if citations[mid]<n-mid:
                lo = mid+1
            else:
                hi = mid
        if citations[hi]>=n-hi:
            return n-hi
        else:
            return 0
# @lc code=end

