#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#
from typing import List
# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        # set every point point to itself
        root = [i for i in range(n)]
        for i in range(n):
            if graph[i]:
                x = self.findRoot(root, i)
                y = self.findRoot(root, graph[i][0])
                if x==y:
                    return False
                for j in range(1, len(graph[i])):
                    parent = self.findRoot(root, graph[i][j])
                    if x == parent:
                        return False
                    root[parent] = y

        return True

    def findRoot(self, root, i):
        if i == root[i]:
            return i
        return self.findRoot(root, root[i])

# @lc code=end

graph = [[1,3], [0,2], [1,3], [0,2]]
graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
res = Solution().isBipartite(graph)
print(res)