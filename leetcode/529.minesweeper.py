#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#
from typing import List
# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or not board[0]:
            return []

        h = len(board)
        w = len(board[0])
        row = click[0]
        col = click[1]
        cnt = 0
        if board[row][col] == 'M':
            board[row][col] = 'X'
        else:
            neighbors = []
            for i in range(-1, 2):
                if row+i<0 or row+i>=h:
                    continue
                for j in range(-1, 2):
                    if col+j<0 or col+j>=w:
                        continue
                    if board[row+i][col+j]=='M':
                        cnt += 1
                    elif board[row+i][col+j]=='E' and cnt==0:
                        neighbors.append([row+i, col+j])
            if cnt>0:
                board[row][col] = str(cnt)
            else:
                for nei in neighbors:
                    board[nei[0]][nei[1]] = 'B'
                    self.updateBoard(board, nei)
        return board

# @lc code=end

board = [
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'M', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E']
]
click = [3,0]

board = [
    ['B', '1', 'E', '1', 'B'],
    ['B', '1', 'M', '1', 'B'],
    ['B', '1', '1', '1', 'B'],
    ['B', 'B', 'B', 'B', 'B']
]
click = [1,2]


res = Solution().updateBoard(board, click)
print(res)