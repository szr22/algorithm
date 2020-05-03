#
# @lc app=leetcode id=553 lang=python3
#
# [553] Optimal Division
#

# @lc code=start
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if not nums:
            return ''
        res = str(nums[0])
        n = len(nums)
        if n == 1:
            return res
        if n == 2:
            return res + '/' + str(nums[1])
        res += '/(' + '/'.join(map(str, nums[1:])) + ')'
        return res

# @lc code=end

