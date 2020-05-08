#
# @lc app=leetcode id=689 lang=python3
#
# [689] Maximum Sum of 3 Non-Overlapping Subarrays
#
from typing import List
import sys
# @lc code=start
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        maxTotal = -sys.maxsize
        res = []
        sums = [0]
        # index of the left and right
        left = [0 for i in range(n)]
        right = [n-k for i in range(n)]

        for num in nums:
            sums.append(num+sums[-1])

        total = sums[k]-sums[0]
        for i in range(k, n):
            if sums[i+1] - sums[i+1-k]>total:
                left[i] = i+1-k
                total = sums[i+1] - sums[i+1-k]
            else:
                left[i] = left[i-1]
        print(left)

        total = sums[n]-sums[n-k]
        for i in range(n-1-k,-1,-1):
            if sums[i+k] - sums[i] >= total:
                right[i] = i
                total = sums[i+k] - sums[i]
            else:
                right[i] = right[i+1]
        print(right)

        for i in range(k, n-2*k+1):
            lIdx = left[i-1]
            rIdx = right[i+k]
            mid = sums[i+k] - sums[i]
            l = sums[lIdx+k] - sums[lIdx]
            r = sums[rIdx+k] - sums[rIdx]
            total = mid+l+r
            if maxTotal < total:
                maxTotal = total
                res = (lIdx, i, rIdx)
        return res

# @lc code=end

nums = [1,2,1,2,6,7,5,1]
k = 2
res = Solution().maxSumOfThreeSubarrays(nums, k)
print(res)