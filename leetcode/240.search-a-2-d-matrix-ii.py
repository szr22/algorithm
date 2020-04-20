#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        height = len(matrix)
        width = len(matrix[0])
        for y in range(height):
            if matrix[y][0] > target:
                return False
            if matrix[y][-1] < target:
                continue
            start, end = 0, width-1
            while start <= end:
                mid = (start+end)//2

                if matrix[y][mid] == target:
                    return True
                if matrix[y][mid] > target:
                    end = mid-1
                else:
                    start = mid+1
        return False

# @lc code=end

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 9
res = Solution().searchMatrix(matrix, target)
print(res)