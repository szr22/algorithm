#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0
        n = len(nums)
        while right<n-1:
            if nums[right]!=nums[right+1]:
                nums[left+1] = nums[right+1]
                left += 1
                right += 1
            else:
                right+=1
        return left+1
# @lc code=end

nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,2]
res = Solution().removeDuplicates(nums)
print(res)