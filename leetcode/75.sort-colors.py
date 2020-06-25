#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, blue = 0, len(nums)-1
        idx = 0
        while idx<=blue:
            if nums[idx] == 0:
                nums[idx], nums[red] = nums[red], nums[idx]
                red += 1
            elif nums[idx] == 2:
                nums[idx], nums[blue] = nums[blue], nums[idx]
                blue -= 1
                idx -= 1
            idx += 1


# @lc code=end

