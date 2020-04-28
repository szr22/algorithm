#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
from typing import List
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        lmax, rmax = 0, 0
        start, end = 0, len(height)-1

        while start<=end:
            lmax = max(lmax, height[start])
            rmax = max(rmax, height[end])
            if lmax <= rmax:
                res += lmax - height[start]
                start += 1
            else:
                res += rmax - height[end]
                end -= 1
        return res

# @lc code=end

class Solution2:
    def trap(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        lmax, rmax = 0, 0
        res = 0
        while start<end:
            lmax = max(lmax, height[start])
            rmax = max(rmax, height[end])
            if lmax>rmax:
                res += rmax-height[end]
                end -= 1
            else:
                res += lmax-height[start]
                start += 1
        return res

height = [0,1,0,2,1,0,1,3,2,1,2,1]
res = Solution2().trap(height)
print(res)