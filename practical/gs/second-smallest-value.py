import heapq
import collections
import sys
import random

class Solution:
    def __init__(self):
        self.heap = []

    def findSecondSmallest(self, arr):
        smallFirst = sys.maxsize
        smallSecond = sys.maxsize
        for num in arr:
            if num < smallFirst:
                smallSecond = smallFirst
                smallFirst = num
            elif num >= smallFirst and (not smallSecond or num < smallSecond):
                smallSecond = num
            # print(smallFirst, smallSecond)

        return smallSecond

    def addToHeap(self, num):
        heapq.heappush(self.heap, num)

        if len(self.heap) > 2:
            tmp = heapq._heappop_max(self.heap)
            print(tmp)
            print(self.heap)


nums = [i for i in range(10)]
# nums.reverse()
random.shuffle(nums)
res = Solution().findSecondSmallest(nums)
# print(res)

from queue import PriorityQueue

pq = PriorityQueue(3)
for i in range(10):
    pq.put(i, False)
    if pq.qsize() ==3:
        pq.get(False)
print(pq.queue)