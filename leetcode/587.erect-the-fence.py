#
# @lc app=leetcode id=587 lang=python3
#
# [587] Erect the Fence
#
from typing import List
# @lc code=start
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        # initialize
        res = []
        first = points[0]
        firstIdx = 0
        n = len(points)

        # find most left point
        for i in range(n):
            if points[i][0] < first[0]:
                first = points[i]
                firstIdx = i

        res.append(first)
        cur = first
        curIdx = firstIdx

        while True:
            nxt = points[0]
            nxtIdx = 0
            for i in range(1, n):
                if i==curIdx:
                    continue
                cross = self.crossProduct(cur, points[i], nxt)
                if (
                    nxtIdx==curIdx
                    or cross>0
                    or (
                            cross==0
                            and self.dist(points[i], cur) > self.dist(nxt, cur)
                        )
                ):
                    nxt = points[i]
                    nxtIdx = i

            for i in range(n):
                if i == curIdx:
                    continue
                cross = self.crossProduct(cur, points[i], nxt)
                if cross == 0:
                    if self.check(res, points[i]):
                        res.append(points[i])

            cur = nxt
            curIdx = nxtIdx
            if curIdx == firstIdx:
                break

        return res

    def crossProduct(self, pointA, pointB, pointC):
        bax = pointA[0] - pointB[0]
        bay = pointA[1] - pointB[1]
        bcx = pointC[0] - pointB[0]
        bcy = pointC[1] - pointB[1]

        return bax*bcy - bay*bcx

    def dist(self, pointA, pointB):
        return (
            (pointA[0]-pointB[0])*(pointA[0]-pointB[0])
            + (pointA[1]-pointB[1])*(pointA[1]-pointB[1])
        )

    def check(self, res, point):
        for p in res:
            if p[0] == point[0] and p[1] == point[1]:
                return False
        return True


    def outerTreesBetter(self, points: List[List[int]]) -> List[List[int]]:
        def is_less_180(x1, y1, x2, y2, x3, y3):
            v1 = (x2-x1, y2-y1)
            v2 = (x3-x2, y3-y2)
            return v1[0]*v2[1]-v1[1]*v2[0] >= 0
        points.sort()
        res1 = []
        for p in points:
            while len(res1) >= 2 and not is_less_180(res1[-2][0], res1[-2][1], res1[-1][0], res1[-1][1], p[0], p[1]):
                res1.pop()
            res1.append((p[0], p[1]))
        res2 = []
        for p in points[::-1]:
            while len(res2) >= 2 and not is_less_180(res2[-2][0], res2[-2][1], res2[-1][0], res2[-1][1], p[0], p[1]):
                res2.pop()
            res2.append((p[0], p[1]))
        return list(set(res1+res2))

# @lc code=end

points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
res = Solution().outerTrees(points)
print(res)