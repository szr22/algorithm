#
# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#

# @lc code=start
class MyCalendarTwo:
    def __init__(self):
        self.event_set = set()
        self.over_lap_set = set()

    def book(self, start: int, end: int) -> bool:
        for over_lap in self.over_lap_set:
            if start >= over_lap[1] or end <= over_lap[0]:
                continue
            return False

        for event in self.event_set:
            if start >= event[1] or end <= event[0]:
                continue
            self.over_lap_set.add((max(start, event[0]), min(end, event[1])))

        self.event_set.add((start, end))
        return True



from collections import defaultdict, OrderedDict
class MyCalendarTwo2:
    def __init__(self):
        self.ts_freq = OrderedDict(int)

    def book(self, start: int, end: int) -> bool:
        self.ts_freq[start] += 1
        self.ts_freq[end] -= 1
        cnt = 0
        for ts in self.ts_freq.keys():
            cnt += self.ts_freq[ts]
            if cnt == 3:
                self.ts_freq[start] -= 1
                self.ts_freq[end] += 1
                return False

        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# @lc code=end