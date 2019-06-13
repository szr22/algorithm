# Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

# Note:
# If n is the length of array, assume the following constraints are satisfied:

# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# Examples:

# Input:
# nums = [7,2,5,10,8]
# m = 2

# Output:
# 18

# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.

from typing import List
from sys import maxsize

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        while left<right:
            mid = left+(right-left)//2
            if self.canSplit(nums, m, mid):
                right = mid
            else:
                left = mid+1
        return left

    def canSplit(self, nums: List[int], m: int, totalSum: int) -> bool:
        cnt = 1
        curSum = 0
        for num in nums:
            curSum += num
            if curSum > totalSum:
                curSum = num
                cnt += 1
                if cnt > m:
                    return False
        return True

    def splitArray2(self, nums: List[int], m: int) -> int:
        n = len(nums)
        sums = [0] * (n+1)
        dp = [[maxsize for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = 0
        for i in range(1, n+1):
            sums[i] = sums[i-1]+nums[i-1]

        for i in range(1, m+1):
            for j in range(1, n+1):
                for k in range(i-1, j):
                    val = max(dp[i-1][k], sums[j]-sums[k])
                    dp[i][j] = min(dp[i][j], val)
        return dp[m][n]

nums = [7,2,5,10,8]
m = 2
res = Solution().splitArray2(nums, m)
print(res)