#
# @lc app=leetcode id=685 lang=python3
#
# [685] Redundant Connection II
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        hashmap = defaultdict(int)
        first = None
        second = None
        for edge in edges:
            if hashmap[edge[1]] == 0:
                hashmap[edge[1]] = edge[0]
            else:
                # find dup edge with two direction
                first = [hashmap[edge[1]], edge[1]]
                second = edge.copy()
                edge[1] = 0

        for i in range(n):
            hashmap[i+1] = i+1
        print(edges)
        for edge in edges:
            # skip the dup edge
            if edge[1]==0:
                continue
            root1 = self.findRoot(edge[0], hashmap)
            root2 = self.findRoot(edge[1], hashmap)
            if root1==root2:
                return first if first else edge
            # order doens't matter
            hashmap[root2]=root1

        return second


    def findRoot(self, node, hashmap):
        while node != hashmap[node]:
            node = hashmap[node]
        return node

# @lc code=end


edges = [[1,2], [1,3], [2,3]]
# edges = [[1,2], [2,3], [3,4], [4,1], [1,5]]
edges = [[2,1],[3,1],[4,2],[1,4]]
edges = [[1,2],[1,3],[2,3]]
res = Solution().findRedundantDirectedConnection(edges)
print(res)