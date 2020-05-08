#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
from typing import List
# @lc code=start

class Trie:
    def __init__(self):
        self.node = {}
    def add(self, word):
        cur = self.node
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                cur[c] = {}
                cur = cur[c]
        if '#' not in cur:
            cur['#'] = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        if not board or not board[0]:
            return []

        trie = Trie()
        for word in words:
            trie.add(word)

        # print(trie.node)

        h = len(board)
        w = len(board[0])
        self.board = board
        self. res = set()
        for i in range(h):
            for j in range(w):
                self.dfs(i, j, h, w, trie.node)
        return list(self.res)

    def dfs(self, row, col, h, w, node):
        if row<0 or row>=h or col<0 or col>=w or self.board[row][col]=='#':
            return

        cur = self.board[row][col]

        if cur not in node:
            return

        if '#' in node[cur]:
            self.res.add(node[cur]['#'])

        self.board[row][col] = '#'

        self.dfs(row-1, col, h, w, node[cur])
        self.dfs(row, col-1, h, w, node[cur])
        self.dfs(row+1, col, h, w, node[cur])
        self.dfs(row, col+1, h, w, node[cur])

        self.board[row][col] = cur


# @lc code=end

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

board = [["a","b"],["a","a"]]
words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]

res = Solution().findWords(board, words)
print(res)