#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
from typing import List
import sys

# @lc code=start
class Solution:
    def jump_tle(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        max_pos = 0
        min_steps = [sys.maxsize] * n
        min_steps[0] = 0

        for i, num in enumerate(nums):
            max_pos = max(max_pos, i+num)
            if max_pos >= n-1:
                return min(min_steps[-1], min_steps[i]+1)
            end = i+num+1
            for j in range(i+1, end):
                min_steps[j] = min(min_steps[j], min_steps[i]+1)

    def jump(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        if n<=1:
            return 0
        last = 0
        cur = 0
        for i in range(n):
            print(last)
            cur = max(cur, i+nums[i])
            if i == last:
                last = cur
                res += 1
                if cur >= n-1:
                    break
        return res

# @lc code=end
arr = [2,3,1,1,4]
res = Solution().jump(arr)
print(res)