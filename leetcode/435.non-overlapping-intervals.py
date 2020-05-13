#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        n = len(intervals)
        last = 0
        intervals.sort()
        for i in range(1, n):
            if intervals[i][0]<intervals[last][1]:
                res += 1
                if intervals[i][1]<intervals[last][1]:
                    last = i
            else:
                last = i
        return res

    def eraseOverlapIntervalsDp(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()
        res = 0
        n = len(intervals)
        endLast = intervals[0][1]
        for i in range(1, n):
            tmp = 0
            if endLast>intervals[i][0]:
                tmp = 1
            if tmp == 1:
                endLast = min(endLast, intervals[i][1])
            else:
                endLast = intervals[i][1]
            res += tmp
        return res

# @lc code=end

