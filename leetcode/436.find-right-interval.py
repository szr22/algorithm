#
# @lc app=leetcode id=436 lang=python3
#
# [436] Find Right Interval
#
from collections import defaultdict
import bisect
# @lc code=start
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = []
        starts = sorted(
            (intv[0], i) for i, intv in enumerate(intervals)
        )

        for intv in intervals:
            key = bisect.bisect_left(starts, (intv[1],))
            if key == len(intervals):
                res.append(-1)
            else:
                res.append(starts[key][1])
        return res


    def findRightIntervalStraight(self, intervals):
        start_map = {interval.start : i for i, interval in enumerate(intervals)}
        start_list = [interval.start for interval in intervals]
        res = []
        start_list.sort()
        for interval in intervals:
            pos = self.higher_find(start_list, interval.end)
            res.append(start_map[start_list[pos]] if pos != -1 else -1)
        return res

    def higher_find(self, array, v):
        lo, hi = 0, len(array) - 1
        first = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if array[mid] >= v:
                hi = mid - 1
                first = mid
            else:
                lo = mid + 1
        return first

# @lc code=end

