#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res = [intervals[0]]
        n = len(intervals)
        for idx in range(1, n):
            if intervals[idx][0]<=res[-1][1]:
                res[-1][1] = max(intervals[idx][1], res[-1][1])
            else:
                res.append(intervals[idx])
        return res

# @lc code=end

