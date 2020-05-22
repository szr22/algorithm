#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        curMax = float('-inf')
        finalMax = float('-inf')
        for num in A:
            curMax = max(0, curMax)+num
            finalMax = max(curMax, finalMax)

        curMin = float('inf')
        finalMin = float('inf')
        for num in A:
            curMin = min(0, curMin+num)
            finalMin = min(finalMin, curMin)

        return max(finalMax, sum(A) - finalMin)
# @lc code=end

