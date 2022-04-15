#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.cum_sum = list(itertools.accumulate([0] + nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.cum_sum[right + 1] - self.cum_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

