#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        self.target = target
        self.nums = nums
        return self.search_binary(0, len(nums)-1)

    def search_binary(self, start, end) -> int:
        if start == end:
            return start if self.nums[start]==self.target else -1
        if end - start == 1:
            if self.nums[start] == self.target:
                return start
            elif self.nums[end] == self.target:
                return end
            else:
                return -1

        mid = (end+start)//2-1

        if self.nums[start] <= self.nums[mid]:
            if self.nums[start] <= self.target and self.nums[mid] >= self.target:
                return self.search_binary(start, mid+1)
            else:
                return self.search_binary(mid+1, end)
        elif self.nums[mid+1] <= self.nums[end]:
            if self.nums[mid+1] <= self.target and self.nums[end] >= self.target:
                return self.search_binary(mid+1, end)
            else:
                return self.search_binary(start, mid+1)

        return -1

    def search_with_pivot(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot = self.find_pivot(nums, 0, n-1)
        if pivot == -1:
            return self.binary_search(nums, 0, n-1, target)
        print(pivot)
        if nums[pivot] == target:
            return pivot
        if nums[0] <= target:
            return self.binary_search(nums, 0, pivot-1, target)
        else:
            return self.binary_search(nums, pivot+1, n-1, target)

    def find_pivot(self, nums, start, end):
        if start > end:
            return -1
        if start == end:
            return start
        mid = (start+end)//2

        if start < mid and nums[mid] < nums[mid-1]:
            return mid-1
        if mid < end and nums[mid] > nums[mid+1]:
            return mid

        if nums[start] >= nums[mid]:
            return self.find_pivot(nums, start, mid-1)
        else:
            return self.find_pivot(nums, mid+1, end)

    def binary_search(self, nums, start, end, target):
        print(start, end)
        if start > end:
            return -1

        mid = (start+end)//2

        if nums[mid]==target:
            return mid
        if nums[mid] > target:
            return self.binary_search(nums, start, mid-1, target)
        else:
            return self.binary_search(nums, mid+1, end, target)
# @lc code=end

nums = [4,5,6,7,0,1,2]
target = 0

# nums = [3,5,1]
# target = 1
res = Solution().search(nums, target)
print(res)