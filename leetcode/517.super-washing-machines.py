#
# @lc app=leetcode id=517 lang=python3
#
# [517] Super Washing Machines
#
from typing import List
# @lc code=start
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)
        if n == 0 or total % n != 0:
            return -1
        res = 0
        cnt = 0
        avg = total // n
        for m in machines:
            cnt += m-avg
            res = max(res, max(abs(cnt), m-avg))
        return res

    def findMinMovesBetter(self, machines: List[int]) -> int:
        n = len(machines)
        if n == 0:
            return -1
        total = [0, machines[0]]
        for i in range(1, n):
            total.append(machines[i]+total[i])
        if total[-1] % n != 0:
            return -1
        res = 0
        avg = total[-1] // n
        for i in range(n):
            lCnt = total[i] - avg*i
            rCnt = total[-1] - total[i+1] - avg*(n-1-i)
            if lCnt>0 and rCnt>0:
                res = max(res, max(lCnt, rCnt))
            elif lCnt<0 and rCnt<0:
                res = max(res, 0 - lCnt - rCnt)
            else:
                res = max(res, max(abs(lCnt), abs(rCnt)))
        return res

# @lc code=end

machines = [6, 3, 6]
machines = [3, 6, 3]
res = Solution().findMinMoves(machines)
print(res)