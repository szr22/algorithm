#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
from typing import List
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        ends = [nums[0]]
        for num in nums:
            if num < ends[0]:
                ends[0] = num
            elif num > ends[-1]:
                ends.append(num)
            else:
                left = 0
                right = len(ends)
                while left<right:
                    mid = (left+right) // 2
                    if ends[mid] < num:
                        left = mid+1
                    else:
                        right = mid
                ends[right] = num
            print(ends)
        return len(ends)

    def lengthOfLISBisect(self, nums):
        if not nums:
            return 0
        dp = list()
        for val in nums:
            if not dp or val > dp[-1]:
                dp.append(val)
            else:
                insert_point = bisect_left(dp, val)
                dp[insert_point] = val
        return len(dp)


    def lengthOfLISdp(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(dp[i], res)
        print(dp)
        return res

# @lc code=end

nums = [10,9,2,5,3,7,101,18]
# nums = [0]
res = Solution().lengthOfLIS(nums)
print(res)