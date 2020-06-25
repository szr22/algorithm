#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
from typing import List
# @lc code=start
class Solution:
    def __init__(self):
        self.dics = [[-1,0],[0,-1],[0,1],[1,0]]

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        h, w = len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if i>0 and i<h-1 and j>0 and j<w-1:
                    continue
                if board[i][j]=="O":
                    self.dfs(board, i, j)
        for i in range(h):
            for j in range(w):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "E":
                    board[i][j] = "O"

    def dfs(self, board, i, j):
        if board[i][j] != "O":
            return
        h, w = len(board), len(board[0])
        board[i][j] = "E"
        for d in self.dics:
            i1 = d[0]+i
            j1 = d[1]+j
            if i1>=0 and i1<h and j1>=0 and j1<w:
                self.dfs(board, i1, j1)

# @lc code=end

