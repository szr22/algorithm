#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
from typing import List
# @lc code=start
class Solution:
    def minSubArrayLenStraight(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        res = float('inf')
        left = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            while left<=i and total>=s:
                res = min(res, i-left+1)
                total -= nums[left]
                left += 1
            # print(total)
        if res == float('inf'):
            return 0
        else:
            return res

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        totals = [0]
        res = n+1
        for i in range(1, n+1):
            totals.append(totals[i-1]+nums[i-1])
        print(totals)
        for i in range(n+1):
            right = self.searchRight(i+1, n, totals[i]+s, totals)
            if right == n+1:
                break
            if res>right-i:
                res = right-i
            # print(res)
        if res == n+1:
            return 0
        return res

    def searchRight(self, left, right, key, totals):
        print(key)
        while left<=right:
            mid = (left+right)//2
            if totals[mid]>=key:
                right = mid-1
            else:
                left = mid+1
        return left


# @lc code=end
s = 11
nums = [1,2,3,4,5]
res = Solution().minSubArrayLen(s, nums)
print(res)