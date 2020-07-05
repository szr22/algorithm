#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicateBinary(self, nums: List[int]) -> int:
        lo, hi = 1, len(nums)
        while lo<hi:
            mid = (lo+hi)//2
            cnt = 0
            for num in nums:
                if num<=mid:
                    cnt += 1
            if cnt <= mid:
                lo = mid+1
            else:
                hi = mid
        return hi

    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        t = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        while True:
            slow = nums[slow]
            t = nums[t]
            if slow == t:
                break
        return slow

    def findDuplicateBit(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(32):
            bit = 1<<i
            cnt1, cnt2 = 0, 0
            for k in range(n):
                if k&bit >0:
                    cnt1 += 1
                if nums[k]&bit>0:
                    cnt2 += 1
            if cnt2>cnt1:
                res += bit
        return res

# @lc code=end

