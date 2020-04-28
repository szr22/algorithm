#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

from typing import List
import sys
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        left, right = (len1+len2+1)//2, (len1+len2+2)//2
        return (
            self.findKthEle(nums1, 0, nums2, 0, left) +
            self.findKthEle(nums1, 0, nums2, 0, right)
        ) / 2

    def findKthEle(self, nums1, idx1, nums2, idx2, k):
        if idx1 >= len(nums1):
            return nums2[idx2 + k - 1]
        if idx2 >= len(nums2):
            return nums1[idx1 + k - 1]
        if k == 1:
            return min(nums1[idx1], nums2[idx2])

        mid1 = sys.maxsize
        if idx1 + k//2-1 < len(nums1):
            mid1 = nums1[idx1 + k//2-1]

        mid2 = sys.maxsize
        if idx2 + k//2-1 < len(nums2):
            mid2 = nums2[idx2 + k//2-1]

        if mid1 < mid2:
            return self.findKthEle(nums1, idx1+k//2, nums2, idx2, k-k//2)
        else:
            return self.findKthEle(nums1, idx1, nums2, idx2+k//2, k-k//2)


# @lc code=end
nums1 = [1, 2]
nums2 = [3, 4]
res = Solution().findMedianSortedArrays(nums1, nums2)
print(res)

