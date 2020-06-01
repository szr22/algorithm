#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        res = []
        graph = defaultdict(set)
        q = []
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)
        # print(graph)
        for i in range(n):
            if len(graph[i])==1:
                q.append(i)

        while n>2:
            cnt = len(q)
            n -= cnt
            for i in range(cnt):
                node = q.pop(0)
                for nei in list(graph[node]):
                    graph[nei].remove(node)
                    if len(graph[nei])==1:
                        q.append(nei)
                    # print(q)
        while q:
            res.append(q.pop(0))

        return res

# @lc code=end

n = 4
edges = [[1,0],[1,2],[1,3]]
res = Solution().findMinHeightTrees(n, edges)
print(res)