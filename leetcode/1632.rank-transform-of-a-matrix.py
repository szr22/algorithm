#
# @lc app=leetcode id=1632 lang=python3
#
# [1632] Rank Transform of a Matrix
#

# @lc code=start
from collections import defaultdict

class DSU:
    def __init__(self):
        self.parent = defaultdict(set)
        self.edges = []

    def add_edge(self, edge):
        """Add element end unify their colum and row"""
        self.edges.append(edge)
        i, j = edge
        self.parent[self.find(i)] = self.find(~j)

    def find(self, x):
        """get set id for x"""
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def components(self):
        """
        Returns a partition of the elements according to the rows / columns
        they are associated with.
        """
        component_list = defaultdict(list)
        for i, j in self.edges:
            component_list[self.find(i)].append((i, j))
        yield from component_list.values()

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        # Setup:
        m, n = len(matrix), len(matrix[0])
        answer = [[0] * n for _ in matrix]
        ranks = defaultdict(int)

        # (1) DSU union process:
        DSUs = defaultdict(DSU)
        for i, j in product(range(m), range(n)):
            val = matrix[i][j]
            DSUs[val].add_edge((i, j))

        # (2) Calculate ranks in a greedy manner:
        for _, dsu in sorted(DSUs.items()):
            for component in dsu.components():
                rank = max(ranks[k] for i, j in component for k in [i, ~j]) + 1
                for i, j in component:
                    ranks[i], ranks[~j] = rank, rank
                    answer[i][j] = rank

        return answer
# @lc code=end

