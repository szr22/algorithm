#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#

# @lc code=start
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = nums[-1] - nums[0]
        while left<right:
            mid = (left+right)//2
            cnt = 0
            start = 0
            for i in range(n):
                while start<n and nums[i]-nums[start]>mid:
                    start += 1
                cnt += i-start
            if cnt<k:
                left = mid+1
            else:
                right = mid
        return right

    def smallestDistancePairStraight(self, nums: List[int], k: int) -> int:
        n = len(nums)
        N = 1000000
        cnt = [0 for _ in range(N)]
        for i in range(n):
            for j in range(i+1, n):
                cnt[abs(nums[i]-nums[j])] += 1
        for i in range(N):
            if cnt[i]>=k:
                return i
            k -= cnt[i]
        return -1

# @lc code=end

