#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u1, u2 in dislikes:
            graph[u1-1].append(u2-1)
            graph[u2-1].append(u1-1)
        group = [0]*N
        for i in range(N):
            if group[i] == 0 and not self.dfs(graph, group, i, 1):
                return False
        return True

    def dfs(self, graph, group, node, idx):
        group[node] = idx
        for nei in graph[node]:
            if group[nei] == idx:
                return False
            if group[nei] == 0 and not self.dfs(graph, group, nei, -idx):
                return False
        return True

# @lc code=end

N = 4
dislikes = [[1,2],[1,3],[2,4]]

res = Solution().possibleBipartition(N, dislikes)
print(res)