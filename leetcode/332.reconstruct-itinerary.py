#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
from typing import List
from collections import defaultdict
import heapq
# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for org, des in tickets:
            heapq.heappush(graph[org], des)

        res = []
        self.dfs(graph, 'JFK', res)
        return res[::-1]

    def dfs(self, graph, org, res):
        while graph[org]:
            des = heapq.heappop(graph[org])
            self.dfs(graph, des, res)
        res.append(org)



# @lc code=end

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
res = Solution().findItinerary(tickets)
print(res)