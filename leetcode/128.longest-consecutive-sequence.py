#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
from collections import defaultdict
from typing import List
# @lc code=start
class Solution:
    def longestConsecutive1(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0
        for num in nums:
            if num not in numsSet:
                continue
            numsSet.remove(num)
            pre = num-1
            nxt = num+1
            while pre in numsSet:
                numsSet.remove(pre)
                pre -= 1
            while nxt in numsSet:
                numsSet.remove(nxt)
                nxt += 1
            res = max(res, nxt-pre-1)

        return res

    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashMap = defaultdict(int)
        for num in nums:
            if hashMap[num]>0:
                continue
            left = hashMap[num-1]
            right = hashMap[num+1]

            total = left+right+1
            hashMap[num] = total
            res = max(res, total)

            hashMap[num-left] = total
            hashMap[num+right] = total
        print(hashMap)
        return res

# @lc code=end

nums = [1,2,0,1]
res = Solution().longestConsecutive(nums)
print(res)