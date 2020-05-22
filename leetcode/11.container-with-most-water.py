#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        maxTotal = 0
        while start<end:
            if height[start]<height[end]:
                maxTotal = max(maxTotal, height[start] * (end-start))
                start+=1
            else:
                maxTotal = max(maxTotal, height[end] * (end-start))
                end-=1

        return maxTotal

# @lc code=end

