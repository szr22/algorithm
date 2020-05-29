#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        h, w = len(obstacleGrid), len(obstacleGrid[0])
        cur = [0 for _ in range(w)]
        for i in range(w):
            if obstacleGrid[0][i]==1:
                break
            else:
                cur[i] = 1
        for r in range(1, h):
            tmp =[]
            if obstacleGrid[r][0]==1:
                tmp.append(0)
            else:
                tmp.append(cur[0])

            for c in range(1, w):
                if obstacleGrid[r][c]==1:
                    tmp.append(0)
                else:
                    tmp.append(cur[c]+tmp[c-1])
            cur = tmp
        return cur[-1]
# @lc code=end

