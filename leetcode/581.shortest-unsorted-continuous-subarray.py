#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarrayTLE(self, nums: List[int]) -> int:
        res = 0
        start = -1
        n = len(nums)
        for i in range(1, n):
            if nums[i]<nums[i-1]:
                j = i
                while j>0 and nums[j]<nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    j -= 1

                if start == -1 or start>j:
                    start = j
                res = i - start + 1
        return res

    def findUnsortedSubarrayBetter(self, nums: List[int]) -> int:
        nums_copy = nums.copy()
        nums_copy.sort()
        start, end = 0, len(nums)-1
        while start<len(nums) and nums[start] == nums_copy[start]:
            start += 1
        while end > start and nums[end] == nums_copy[end]:
            end -= 1
        return end-start+1

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = -1
        right = -2
        mn = nums[n-1]
        mx = nums[0]
        for i in range(1, n):
            mx = max(mx, nums[i])
            if mx > nums[i]:
                right = i

            mn = min(mn, nums[n-i-1])
            if mn < nums[n-i-1]:
                left = n-i-1
        return right-left+1





# @lc code=end

