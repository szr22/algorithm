#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        idx = len(nums1)-1
        end1 = m-1
        end2 = n-1
        while end2>=0 and end1>=0:
            if nums2[end2]>nums1[end1]:
                nums1[idx]=nums2[end2]
                end2-=1
            else:
                nums1[idx]=nums1[end1]
                end1-=1
            idx-=1

        while end2>=0:
            nums1[idx]=nums2[end2]
            end2-=1
            idx-=1

# @lc code=end

nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)
