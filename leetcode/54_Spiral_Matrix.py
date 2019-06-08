# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix or not matrix[0]:
            return res
        h = len(matrix)
        w = len(matrix[0])
        # start from -1, 0
        x, y = -1, 0
        while True:
            for i in range(w):
                x += 1
                res.append(matrix[y][x])
            h -= 1
            if h == 0:
                break
            for i in range(h):
                y += 1
                res.append(matrix[y][x])
            w -= 1
            if w == 0:
                break
            for i in range(w):
                x -= 1
                res.append(matrix[y][x])
            h -= 1
            if h == 0:
                break
            for i in range(h):
                x -= 1
                res.append(matrix[y][x])
            w -= 1
            if w == 0:
                break
        return res

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

res = Solution().spiralOrder(matrix)
print(res)