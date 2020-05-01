#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#
from typing import List
# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        dirc = 0
        if n<=1:
            return True
        for i in range(1,n):
            if A[i]<A[i-1]:
                if dirc == 0 or dirc==1:
                    dirc = 1
                else:
                    return False
            if A[i]>A[i-1]:
                if dirc == 0 or dirc==-1:
                    dirc = -1
                else:
                    return False
        return True

    def isMonotonic2(self, nums):
        n = len(A)
        if n<=1:
            return True
        inc = True
        dec = True
        for i in range(1, n):
            inc &= (nums[i - 1] <= nums[i])
            dec &= (nums[i - 1] >= nums[i])
            if not inc and not dec:
                return False
        return True

# @lc code=end

A = [1,2,4,5]
A = [1,3,2]
A = [6,5,4,4]
# A = [1,2,2,3]
A = []
A = [1,1]


res = Solution().isMonotonic2(A)
print(res)