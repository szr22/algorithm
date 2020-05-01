#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [1 for _ in range(n)]
        r = [1 for _ in range(n)]
        for i in range(1,n):
            l[i] = l[i-1]*nums[i-1]
        for i in range(n-2, -1, -1):
            r[i] = r[i+1] * nums[i+1]

        for i in range(n):
            nums[i] = l[i]*r[i]
        return nums

# @lc code=end

