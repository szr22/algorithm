#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        self.queens = [['.' for _ in range(n)] for _ in range(n)]
        self.helper(0)
        return self.res

    def helper(self, curRow):
        # print(self.queens)
        n = len(self.queens)
        if curRow == n:
            self.res += 1
            return
        for i in range(n):
            if self.isValid(curRow, i):
                self.queens[curRow][i] = 'Q'
                self.helper(curRow+1)
                self.queens[curRow][i] = '.'

    def isValid(self, row, col):
        # check col
        for i in range(row):
            if self.queens[i][col] == 'Q':
                return False
        # check dia
        i = row-1
        j = col-1
        while i>=0 and j>=0:
            if self.queens[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # check back dia
        i = row-1
        j = col+1
        while i>=0 and j<len(self.queens):
            if self.queens[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True
# @lc code=end


res = Solution().totalNQueens(4)
print(res)