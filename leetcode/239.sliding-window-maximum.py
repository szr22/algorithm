#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
from typing import List
# @lc code=start
from queue import PriorityQueue
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        for idx, num in enumerate(nums):
            if queue and queue[0] == idx-k:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[idx]:
                queue.pop()

            queue.append(idx)
            if idx - k >= -1:
                res.append(nums[queue[0]])

            print(queue)
        return res

    def maxSlidingWindowPQ(self, nums: List[int], k: int) -> List[int]:
        res = []
        pq = PriorityQueue()
        for idx, num in enumerate(nums):
            while pq.queue and pq.queue[0][1] <= idx-k:
                pq.get()
            pq.put((-num, idx))
            if idx - k >= -1:
                res.append(-pq.queue[0][0])
        return res

# @lc code=end

nums = [1,3,-1,-3,5,3,6,7]
k = 3

res = Solution().maxSlidingWindow(nums, k)
print(res)