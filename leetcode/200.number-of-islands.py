#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

from typing import List

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        self.grid = grid
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == '1':
                    self.check_island(x, y)

                    res += 1
        return res
    
    def check_island(self, x: int, y: int):
        self.grid[y][x] = 0
        if y+1<len(self.grid) and self.grid[y+1][x] == '1':
            self.check_island(x, y+1)
        if x+1<len(self.grid[0]) and self.grid[y][x+1] == '1':
            self.check_island(x+1, y)
        if y-1>=0 and self.grid[y-1][x] == '1':
            self.check_island(x, y-1)
        if x-1>=0 and self.grid[y][x-1] == '1':
            self.check_island(x-1, y)

# @lc code=end
test_grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
res = Solution().numIslands(test_grid)
print(res)