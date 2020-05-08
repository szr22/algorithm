#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def __init__(self):
        self.dirs = [[1,0],[-1,0],[0,-1],[0,1]]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        h = len(grid)
        w = len(grid[0])
        rot = []
        fresh = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j]==2:
                    rot.append([i,j])
                if grid[i][j]==1:
                    fresh += 1
        if fresh == 0:
            return 0
        steps = -1
        while rot:
            size = len(rot)
            for _ in range(size):
                i, j = rot.pop(0)
                for d in self.dirs:
                    ni = i+d[0]
                    nj = j+d[1]
                    if ni<0 or nj<0 or ni>=h or nj>=w or grid[ni][nj]!=1:
                        continue
                    grid[ni][nj]=2
                    rot.append([ni, nj])
                    fresh-=1
            steps+=1
        if fresh!=0:
            return -1
        return steps



# @lc code=end

