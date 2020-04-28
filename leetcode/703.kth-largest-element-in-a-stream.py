#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#
from typing import List
import heapq
# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # self.nums = nums
        # self.k = k
        # heapq.heapify(self.nums)
        self.pool = nums
        self.size = len(self.pool)
        self.k = k
        heapq.heapify(self.pool)
        while self.size > k:
            heapq.heappop(self.pool)
            self.size -= 1

    def add(self, val: int) -> int:
        # heapq.heappush(self.nums, val)
        # return heapq.nlargest(self.k, self.nums)[self.k-1]
        if self.size < self.k:
            heapq.heappush(self.pool, val)
            self.size += 1
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

