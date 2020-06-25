#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
import sys
from typing import List
from collections import defaultdict
import heapq
# @lc code=start
class Solution:
    def findCheapestPriceStraight(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for s, d, c in flights:
            graph[s].append((d, c))
        res = sys.maxsize
        q = [(src, 0)]
        steps = 0

        while q:
            size = len(q)
            for _ in range(size, 0, -1):
                cur, cost = q.pop(0)
                if cur == dst:
                    res = min(res, cost)
                for d, c in graph[cur]:
                    if c+cost>res:
                        continue
                    q.append((d, c+cost))

            if steps>K:
                break
            steps += 1
        if res == sys.maxsize:
            return -1
        return res

    def findCheapestPriceBellmanFord(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        kInfCost = 1e9
        costs = [kInfCost for _ in range(n)]
        costs[src] = 0

        for _ in range(K+1):
            tmp = list(costs)
            for s, d, c in flights:
                tmp[d] = min(tmp[d], costs[s]+c)
            costs = tmp
        if costs[dst] == 1e9:
            return -1
        return costs[dst]

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
         # Build the adjacency matrix
        graph = defaultdict(list)
        for s, d, w in flights:
            graph[s].append((d, w))

        # Shortest distances array
        distances = [float("inf") for _ in range(n)]
        current_stops = [float("inf") for _ in range(n)]
        distances[src], current_stops[src] = 0, 0

        # Data is (cost, stops, node)
        minHeap = [(0, 0, src)]

        while minHeap:

            cost, stops, node = heapq.heappop(minHeap)

            # If destination is reached, return the cost to get here
            if node == dst:
                return cost

            # If there are no more steps left, continue
            if stops == K + 1:
                continue

            # Examine and relax all neighboring edges if possible
            for nei, price in graph[node]:
                dU, dV, wUV = cost, distances[nei], price

                    # Better cost?
                if dU + wUV < dV:
                    distances[nei] = dU + wUV
                    heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
                elif stops < current_stops[nei]:

                    #  Better steps?
                    current_stops[nei] = stops
                    heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))

        return -1 if distances[dst] == float("inf") else distances[dst]

# @lc code=end

n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1

# n = 3
# edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 0

res = Solution().findCheapestPrice(n, edges, src, dst, k)
print(res)