#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#
from collections import deque
# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        queue = deque([-1])
        n = len(arr)
        for i in range(n-1, 0, -1):
            if arr[i]>queue[0]:
                queue.appendleft(arr[i])
            else:
                queue.appendleft(queue[0])

        return queue

# @lc code=end

