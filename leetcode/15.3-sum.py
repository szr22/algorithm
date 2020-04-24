#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        start, end = 0, len(nums)-1
        res = []

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            low = i+1
            high = len(nums)-1

            while low<high:
                if nums[low]+nums[high]+nums[i] == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    while low<high and nums[low]==nums[low+1]:
                        low += 1
                    while low<high and nums[high-1]==nums[high]:
                        high -= 1
                    low += 1
                    high -= 1
                elif nums[low]+nums[high]+nums[i] > 0:
                    high -= 1
                else:
                    low += 1
        return res

# @lc code=end

