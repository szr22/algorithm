#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
class Solution:
    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i-1]
        self.w = w
        self.max = w[-1]

    def pickIndex(self) -> int:
        return bisect.bisect_right(self.w,random.randrange(0,self.max))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

class Solution2:
    def __init__(self, w: List[int]):
        self.acc = list(itertools.accumulate(w, operator.add))
        print(self.acc)
        self.max = self.acc[-1]
        print(self.max)

    def pickIndex(self) -> int:
        choice = random.randint(1, self.max)

        left = 0
        right = len(self.acc)

        while (right - left) > 1:
            mid = left + (right - left) // 2
            if self.acc[mid - 1] < choice:
                left = mid
            else:
                right = mid
        return left