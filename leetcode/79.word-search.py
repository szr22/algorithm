#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
from typing import List
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if self.check(board, r, c, word, 0, {(r<<10)+c}):
                        return True
        return False

    def check(self, board, row, col, word, idx, visited):
        if idx==len(word)-1:
            return True
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        idx+=1
        for d in dirs:
            nRow = row+d[0]
            nCol = col+d[1]
            hashcode = (nRow<<10)+nCol
            if (
                nRow>=0
                and nRow<len(board)
                and nCol>=0
                and nCol<len(board[0])
                and hashcode not in visited
                and board[nRow][nCol]==word[idx]
            ):
                visited.add(hashcode)
                if self.check(board, nRow, nCol, word, idx, visited):
                    return True
                visited.remove(hashcode)
        return False

# @lc code=end


board = [
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]
]
word = "ABCEFSADEESE"

res = Solution().exist(board, word)
print(res)
