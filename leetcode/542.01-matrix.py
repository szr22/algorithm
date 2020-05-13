#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        h, w = len(matrix), len(matrix[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        q = []
        for i in range(h):
            for j in range(w):
                if matrix[i][j]==0:
                    q.append([i,j])
                else:
                    matrix[i][j]=sys.maxsize
        while q:
            cur = q.pop(0)
            for d in dirs:
                i = cur[0]+d[0]
                j = cur[1]+d[1]
                if i<0 or i>=h or j<0 or j>=w or matrix[i][j]<=matrix[cur[0]][cur[1]]+1:
                    continue
                matrix[i][j] = matrix[cur[0]][cur[1]]+1
                q.append([i,j])
        return matrix

    def updateMatrixFast(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell:
                    top = matrix[i-1][j] if i else float('inf')
                    left = matrix[i][j-1] if j else float('inf')
                    matrix[i][j] = min(top, left) + 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if cell == matrix[i][j]:
                    bottom = matrix[i+1][j] if i < m - 1 else float('inf')
                    right = matrix[i][j+1] if j < n - 1 else float('inf')
                    matrix[i][j] = min(cell, bottom + 1, right + 1)
        return matrix
# @lc code=end

