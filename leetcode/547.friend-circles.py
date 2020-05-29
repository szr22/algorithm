#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#

# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        res = 0
        visited = [False for _ in range(n)]
        for i in range(n):
            if visited[i]:
                continue
            self.helper(M, i, visited)
            res += 1
        return res

    def helper(self, M, i, visited):
        visited[i] = True
        for j in range(len(M)):
            if not M[i][j] or visited[j]:
                continue
            self.helper(M, j, visited)
# @lc code=end

