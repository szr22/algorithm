#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution:
    def __init__(self):
        self.dirs = [[0,1],[0,-1],[1,0],[-1,0]]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        h, w = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(w)] for _ in range(h)]
        res = 1
        for i in range(h):
            for j in range(w):
                if dp[i][j]>0:
                    continue
                q = [[i,j]]
                cnt = 1
                while q:
                    cnt += 1
                    size = len(q)
                    for _ in range(size):
                        tmp = q.pop(0)
                        for di, dj in self.dirs:
                            y = di+tmp[0]
                            x = dj+tmp[1]
                            if (
                                x<0 or x>=w
                                or y<0 or y>=h
                                or matrix[y][x] <= matrix[tmp[0]][tmp[1]]
                                or cnt <= dp[y][x]
                            ):
                                continue
                            dp[y][x] = cnt
                            res = max(res, cnt)
                            q.append([y,x])
        return res

    def longestIncreasingPathDfs(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        res = 1
        self.h, self.w = len(matrix), len(matrix[0])
        self. matrix = matrix
        self.dp = [[0 for _ in range(self.w)] for _ in range(self.h)]
        for i in range(self.h):
            for j in range(self.w):
                res = max(res, self.dfs(i,j))
        return res

    def dfs(self, i, j):
        if self.dp[i][j]:
            return self.dp[i][j]
        mx = 1
        for dx, dy in self.dirs:
            y = i+dy
            x = j+dx
            if (
                x<0 or x>=self.w
                or y<0 or y>=self.h
                or self.matrix[y][x] <= self.matrix[i][j]
            ):
                continue
            l = 1 + self.dfs(y,x)
            mx = max(mx, l)
        self.dp[i][j] = mx
        return mx


# @lc code=end

