#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
from typing import List
# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        hashMap = dict()
        for num in nums2:
            while stack and stack[-1]<num:
                hashMap[stack[-1]] = num
                stack.pop()
            stack.append(num)
        for num in nums1:
            if num in hashMap:
                res.append(hashMap[num])
            else:
                res.append(-1)
        return res

# @lc code=end

nums1 = [4,1,2]
nums2 = [1,3,4,2]

# nums1 = [2,4]
# nums2 = [1,2,3,4]

res = Solution().nextGreaterElement(nums1, nums2)
print(res)