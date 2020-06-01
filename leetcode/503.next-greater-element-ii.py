#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#
from typing import List
# @lc code=start
class Solution:
    def nextGreaterElementsStraight(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        for i in range(n):
            for j in range(i+1, i+n):
                if nums[j%n]>nums[i]:
                    res[i] = nums[j%n]
                    break
        return res

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        stack = []
        for i in range(2*n):
            num = nums[i%n]
            while stack and nums[stack[-1]]<num:
                res[stack[-1]] = num
                stack.pop()
            if i<n:
                stack.append(i)
            # print(stack)
        return res
# @lc code=end

nums = [3,2,1,2,3]
res = Solution().nextGreaterElements(nums)
print(res)