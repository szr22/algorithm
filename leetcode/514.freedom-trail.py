#
# @lc app=leetcode id=514 lang=python3
#
# [514] Freedom Trail
#

# @lc code=start
class Solution:
    def findRotateStepsStraight(self, ring: str, key: str) -> int:
        lenR = len(ring)
        lenK = len(key)

        dp = [[0 for _ in range(lenR)] for _ in range(lenK+1)]
        for i in range(lenK-1, -1, -1):
            for j in range(lenR):
                dp[i][j] = sys.maxsize
                for k in range(lenR):
                    if ring[k]==key[i]:
                        diff = abs(j-k)
                        step = min(diff, lenR-diff)
                        dp[i][j] = min(dp[i][j], step+dp[i+1][k])
        return dp[0][0]+lenK

    def findRotateSteps(self, ring: str, key: str) -> int:
        lenR = len(ring)
        lenK = len(key)

        memo = [[0 for _ in range(lenK)] for _ in range(lenR)]
        charTable = defaultdict(list)
        for i in range(lenR):
            charTable[ring[i]].append(i)
        return self.helper(ring, key, 0, 0, charTable, memo)

    def helper(self, ring, key, x, y, charTable, memo):
        if y==len(key):
            return 0
        if memo[x][y]>0:
            return memo[x][y]
        res = sys.maxsize
        lenR = len(ring)
        for k in (charTable[key[y]]):
            diff = abs(x-k)
            step = min(diff, lenR-diff)
            res = min(res, step+self.helper(ring, key, k, y+1, charTable, memo))
        memo[x][y] = res+1
        return memo[x][y]
# @lc code=end

