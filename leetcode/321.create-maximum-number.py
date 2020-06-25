#
# @lc app=leetcode id=321 lang=python3
#
# [321] Create Maximum Number
#
from typing import List
# @lc code=start
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n1, n2 = len(nums1), len(nums2)
        res = []
        for i in range(max(k-n2, 0), min(k, n1)+1):
            res = max(
                res,
                self.mergeList(self.maxList(nums1, i), self.maxList(nums2, k-i))
            )
        return res

    def maxList(self, nums, k):
        rmvCnt = len(nums)-k
        res = []
        for num in nums:
            while rmvCnt>0 and res and res[-1]<num:
                res.pop()
                rmvCnt -= 1
            res.append(num)
        return res[:k]

    def mergeList(self, nums1, nums2):
        # print(nums1, nums2)
        res = []
        while nums1 or nums2:
            tmp = nums1 if nums1>nums2 else nums2
            res.append(tmp[0])
            tmp.pop(0)
        return res
# @lc code=end

nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5

# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
res = Solution().maxNumber(nums1, nums2, k)
print(res)