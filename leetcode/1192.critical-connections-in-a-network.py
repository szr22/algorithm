#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#
from collections import defaultdict
from typing import List
# @lc code=start
class Solution:
    def __init__(self):
        self.res = []
        self.graph = defaultdict(list)

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        if not connections or n==1:
            return []

        self.build_graph(connections)
        print(self.graph)
        min_steps = [0] * n
        self.dfs(0, -1, 0, min_steps)

        return self.res

    def build_graph(self, connections):
        for a, b in connections:
            self.graph[a] += [b]
            self.graph[b] += [a]

    def dfs(self, cur, pre, steps, min_steps):
        min_steps[cur] = steps+1
        for neighbor in self.graph[cur]:
            if neighbor == pre:
                continue
            if min_steps[neighbor] == 0:
                tmp = self.dfs(neighbor, cur, steps+1, min_steps)
                min_steps[cur] = min(min_steps[cur], tmp)
                print(min_steps)
            else:
                min_steps[cur] = min(min_steps[cur], min_steps[neighbor])
                print(min_steps)
        if min_steps[cur] == steps+1 and cur != 0:
            self.res.append([pre, cur])
        return min_steps[cur]
# @lc code=end

n = 6
connections = [[0,1],[2,0],[1,3], [4,5]]

res = Solution().criticalConnections(n, connections)
print(res)
