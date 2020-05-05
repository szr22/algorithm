#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#
from collections import defaultdict
import sys
# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hashMap = defaultdict(int)
        res = 0
        for num in nums:
            hashMap[num] += 1
        for num, cnt in hashMap.items():
            if k==0 and cnt>1:
                res+=1
            if k>0 and num+k in hashMap:
                res+=1
        return res

    def findPairsNoMap(self, nums, k):
        res = 0
        n = len(nums)
        j = 0
        pre = sys.maxsize
        nums.sort()
        for i in range(1,n):
            while j<i and nums[i]-nums[j]>k:
                j+=1
            if j!=i and pre!=nums[j] and nums[i]-nums[j]==k:
                res+=1
                pre = nums[j]
        return res

# @lc code=end

