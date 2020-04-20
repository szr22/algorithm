#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
from typing import List
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        for i in range(1, w):
            grid[0][i] = grid[0][i-1]+grid[0][i]
        for i in range(1, h):
            grid[i][0] = grid[i-1][0]+grid[i][0]

        for y in range(1, h):
            for x in range(1, w):
                grid[y][x] = min(
                    grid[y][x-1],
                    grid[y-1][x]
                )+grid[y][x]
        return grid[-1][-1]
# @lc code=end

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

res = Solution().minPathSum(grid)

print(res)