#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo+hi)//2
            cnt = 0
            i  = len(matrix[0])
            for row in matrix:
                while i>=1 and row[i-1]>mid:
                    i -= 1
                cnt += i
            if cnt<k:
                lo = mid+1
            else:
                hi = mid
        return lo
# @lc code=end

