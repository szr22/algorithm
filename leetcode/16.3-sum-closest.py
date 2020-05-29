#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)<3:
            return 0
        nums.sort()
        n = len(nums)
        res = sys.maxsize
        for i in range(n-2):
            left, right = i+1, n-1
            while left<right:
                cur = nums[i]+nums[left]+nums[right]
                if cur == target:
                    return cur
                if cur>target:
                    right -= 1
                else:
                    left += 1
                if abs(cur-target) < abs(res-target):
                    res = cur
        return res
# @lc code=end

