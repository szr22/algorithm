#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
from typing import List
# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        height, width = len(matrix), len(matrix[0])
        res = 0
        sumMatrix = [[0 for _ in range(width)] for _ in range(height)]
        for y in range(height):
            for x in range(width):
                curVal = int(matrix[y][x])
                if y>0:
                    curVal += sumMatrix[y-1][x]
                if x>0:
                    curVal += sumMatrix[y][x-1]
                if x>0 and y>0:
                    curVal -= sumMatrix[y-1][x-1]

                sumMatrix[y][x] = curVal
                cnt = 1
                for _ in range(min(x,y)+1):
                    if res < cnt:
                        sumVal = sumMatrix[y][x]
                        if y-cnt>=0:
                            sumVal -= sumMatrix[y-cnt][x]
                        if x-cnt>=0:
                            sumVal -= sumMatrix[y][x-cnt]
                        if y-cnt>=0 and x-cnt>=0:
                            sumVal += sumMatrix[y-cnt][x-cnt]
                        if sumVal==cnt*cnt:
                            res = max(res, cnt)
                    cnt+=1
        return res*res
# @lc code=end


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["1"]]
res = Solution().maximalSquare(matrix)
print(res)


class SolutionBetter:
    def maximalSquare(self, matrix):
        if (not matrix) or (not matrix[0]):
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        widths = [0] * rows
        max_length = 0
        for j in range(0, cols):
            max_continous_length = 0
            continous_length = 0
            for i in range(0, rows):
                if matrix[i][j] == '1':
                    widths[i] += 1
                else:
                    widths[i] = 0
                if widths[i] > max_length:
                    continous_length += 1
                    max_continous_length = max(continous_length, max_continous_length)
                else:
                    continous_length = 0
            if max_continous_length > max_length:
                max_length += 1
        return max_length * max_length