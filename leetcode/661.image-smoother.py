#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#
from typing import List
# @lc code=start
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        if not M or not M[0]:
            return []
        h, w = len(M), len(M[0])
        res = [[0 for _ in range(w)] for _ in range(h)]
        for y in range(h):
            for x in range(w):
                total = 0
                cnt = 0
                for j in range(-1, 2):
                    if y+j<0 or y+j>=h:
                        continue
                    for i in range(-1, 2):
                        if x+i<0 or x+i>=w:
                            continue
                        total += M[y+j][x+i]
                        cnt += 1
                print(total, cnt)
                res[y][x] = total//cnt
                # print(res)
        return res
# @lc code=end

M = [
    [2,3,4],
    [5,6,7],
    [8,9,10],
    [11,12,13],
    [14,15,16]
]
res = Solution().imageSmoother(M)
print(res)

