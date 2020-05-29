#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSumBad(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
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

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1

        nums = sorted(dic)
        for i, num in enumerate(nums):
            if num == 0:
                if dic[num]>2:
                    res.append([0,0,0])
            else:
                if dic[num]>1 and -2 * num in dic:
                    res.append([num, num, -2*num])

            if num < 0:
                target = -num
                left = bisect.bisect_left(nums, target-nums[-1], i + 1)
                right = bisect.bisect_right(nums, target >> 1, left)
                for num2 in nums[left : right]:
                    # find concrete num3
                    num3 = target - num2
                    # check num3 in dic
                    if num3 in dic and num2 != num3:
                        res.append((num, num2, num3))
        return res
# @lc code=end

