#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#

# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon or not dungeon[0]:
            return 0
        h, w = len(dungeon), len(dungeon[0])
        dp = [sys.maxsize for _ in range(w+1)]
        dp[w-1]=1
        for i in range(h-1, -1, -1):
            for j in range(w-1, -1, -1):
                dp[j] = max(1, min(dp[j], dp[j+1])-dungeon[i][j])
        return dp[0]
# @lc code=end

