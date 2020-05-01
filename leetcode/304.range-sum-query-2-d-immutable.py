#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        h = len(matrix)
        w = len(matrix[0])
        self.sumMatrix = [[0 for _ in range(w+1)] for _ in range(h+1)]
        for y in range(1, h+1):
            for x in range(1, w+1):
                self.sumMatrix[y][x] = (
                    matrix[y-1][x-1]
                    + self.sumMatrix[y-1][x]
                    + self.sumMatrix[y][x-1]
                    - self.sumMatrix[y-1][x-1]
                )



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.sumMatrix[row2+1][col2+1]
            - self.sumMatrix[row1][col2+1]
            - self.sumMatrix[row2+1][col1]
            + self.sumMatrix[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

