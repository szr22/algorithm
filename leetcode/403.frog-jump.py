#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        hashMap = defaultdict(set)
        dp = [0]*n
        hashMap[0].add(0)
        curIdx=0
        for i in range(1, n):
            # curIdx can't reach stones i
            while dp[curIdx]+1+stones[curIdx]<stones[i]:
                curIdx+=1
            for j in range(curIdx, i):
                gap = stones[i]-stones[j]
                if (
                    gap-1 in hashMap[j]
                    or gap in hashMap[j]
                    or gap+1 in hashMap[j]
                ):
                    hashMap[i].add(gap)
                    dp[i] = max(dp[i], gap)
        # print(dp)
        return dp[-1]>0


    def canCrossRecursive(self, stones: List[int]) -> bool:
        self.hashMap = {}
        self.stones = stones
        return self.canCrossRec(0, 0)

    def canCrossRec(self, curPos, step):
        n = len(self.stones)
        key = curPos | step<<11
        if curPos >= n-1:
            return True
        if key in self.hashMap:
            return self.hashMap[key]
        for i in range(curPos+1, n):
            gap = self.stones[i]-self.stones[curPos]
            if gap<step-1:
                continue
            if gap>step+1:

                self.hashMap[key]=False
                return False
            if self.canCrossRec(i, gap):

                self.hashMap[key]=True
                return True

        self.hashMap[key]=False
        return False

# @lc code=end

stones = [0,1,3,5,6,8,12,17]
stones = [0,1,2,3,4,8,9,11]

res = Solution().canCross(stones)
print(res)