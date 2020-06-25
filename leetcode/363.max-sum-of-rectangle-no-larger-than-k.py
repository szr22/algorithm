#
# @lc app=leetcode id=363 lang=python3
#
# [363] Max Sum of Rectangle No Larger Than K
#
from typing import List
import bisect
import sys
# @lc code=start
class Solution:
    def maxSumSubmatrixTLE(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0

        h, w = len(matrix), len(matrix[0])
        res = -sys.maxsize
        dp = [[0 for _ in range(w)] for _ in range(h)]
        for i in range(h):
            for j in range(w):
                t = matrix[i][j]
                if i>0:
                    t += dp[i-1][j]
                if j>0:
                    t += dp[i][j-1]
                if i>0 and j>0:
                    t -= dp[i-1][j-1]
                dp[i][j] = t
                for row in range(i+1):
                    for col in range(j+1):
                        cur = dp[i][j]
                        if row>0:
                            cur -= dp[row-1][j]
                        if col>0:
                            cur -= dp[i][col-1]
                        if row>0 and col>0:
                            cur += dp[row-1][col-1]
                        if cur<=k:
                            res = max(res, cur)
        return res

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0

        h, w = len(matrix), len(matrix[0])
        res = -sys.maxsize
        mx = max(h,w)
        mn = min(h,w)
        for i in range(mn):
            sums = [0] * mx
            for j in range(i, mn):
                slist, num = [], 0
                for l in range(mx):
                    if h>w:
                        sums[l] += matrix[l][j]
                    else:
                        sums[l] += matrix[j][l]
                    num += sums[l]
                    if num<=k:
                        res = max(res, num)
                    i = bisect.bisect_left(slist, num-k)
                    if i !=len (slist):
                        res = max(res, num-slist[i])
                    bisect.insort(slist, num)
        return res

# @lc code=end

matrix = [[9,-10,-3,-1,1,7,-6,-2,1,-4,-6,-8,-1,2,-9,-7,-9,-1,-1,5,-4,5,-8,3,4,2,9,4,5,4,-8,5,4,-9,-10,3,-2,-2,9,0,-4,3,5,-10,8,-10,9,-7,-6,1,2,6,-8,1,7,3,0,-5,7,-6,1,9,-8,4,-7,-9,1,8,-2,6,-1,0,8,4,-9,8,-3,7,-4,3,-6,2,-1,-2,-10,-10,-10,-3,8,2,-4,3,-6,-3,1,9,-9,7,-6,8],[8,-10,-4,-5,7,2,-6,7,-9,0,-8,9,-4,-5,-2,3,2,7,3,3,0,-3,-10,8,-9,3,-6,-9,3,-10,9,9,-3,6,-8,-7,5,5,9,5,-6,6,1,4,4,-5,-1,2,9,-8,8,-9,-9,-6,8,-3,1,0,-7,9,8,-3,-9,-4,8,-2,-9,2,7,-3,0,6,-7,3,3,-8,1,-2,-6,-5,3,6,0,-9,-6,-4,-10,-6,8,3,1,0,-1,-5,-10,5,-2,-5,-10,6],[-3,-5,-1,-8,-7,-6,-6,0,7,0,3,-6,-9,7,-5,-7,8,4,-4,2,7,-4,-6,4,-9,-8,-1,-9,-1,8,3,8,-2,2,-2,5,9,-1,3,-6,8,2,-6,-2,2,2,-8,-2,-2,0,6,2,2,4,-1,-3,-3,4,-2,4,-6,-7,3,2,-6,3,5,-10,-6,7,-4,-4,-3,-5,-8,-7,-9,-8,-7,5,-9,7,8,-10,7,6,6,-1,-3,4,4,-2,3,-1,-9,-10,-5,-7,8,-1],[-8,-3,3,7,9,-5,3,5,-1,-9,5,8,5,2,6,6,-5,-2,-6,5,-2,-5,3,2,-1,-7,5,-3,-6,0,4,-4,-6,9,-6,-9,-10,7,9,3,6,-6,4,-3,-7,-9,-3,6,-3,0,7,9,-7,-3,9,-8,2,7,-9,6,2,8,-5,5,-7,0,-5,3,8,-6,8,-5,-9,-6,-5,-7,5,-3,7,2,3,5,-2,-3,-3,3,4,-4,0,2,-4,3,-3,-6,-2,-3,-4,9,-3,-7]]
k = 292
res = Solution().maxSumSubmatrix(matrix, k)
print(res)