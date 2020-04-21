#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

import math
from typing import List
import heapq

# @lc code=start
class Point:
    def __init__(self, arr):
        self.val = arr
        self.dist = (arr[1])**2 + (arr[0])**2

    def __lt__(self, other):
        return self.dist < other.dist

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            heapq.heappush(heap, Point(point))

        res = []
        for _ in range(K):
            res.append(heapq.heappop(heap).val)
        return res

# @lc code=end

points = [[1,3],[-2,2]]
K = 1

points = [[3,3],[5,-1],[-2,4]]
K = 2

res = Solution().kClosest(points, K)
print(res)