#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#

# @lc code=start
class MyCalendar:

    def __init__(self):
        self.events = set()


    def book(self, start: int, end: int) -> bool:
        for ev in self.events:
            if start >= ev[1] or end <= ev[0]:
                continue
            else:
                return False

        self.events.add((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

