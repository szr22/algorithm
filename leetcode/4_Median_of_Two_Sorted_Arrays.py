# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if (n1+n2)%2 == 0:
            return (self.find_kth(nums1, nums2, (n1+n2)//2)+self.find_kth(nums1, nums2, (n1+n2)//2-1))/2
        else:
            return self.find_kth(nums1, nums2, (n1+n2)//2)
    
    def find_kth(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        if k == 0:
            return min(nums1[0], nums2[0])
        n1 = len(nums1)
        n2 = len(nums2)
        if nums1[n1//2]>nums2[n2//2]:
            if k > n1//2+n2//2:
                return self.find_kth(nums1, nums2[n2//2+1:], k-n2//2-1)
            else:
                return self.find_kth(nums1[:n1//2], nums2, k)
        else:
            return self.find_kth(nums2, nums1, k)

nums1 = [1, 2, 6]
nums2 = [3, 7, 8]

res = Solution().findMedianSortedArrays(nums1, nums2)
print(res)

        